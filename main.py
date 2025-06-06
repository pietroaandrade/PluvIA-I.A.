from openai import OpenAI
import os
from dotenv import load_dotenv
from weatherAnalysis import (
    prepara_prompt, 
    analise_climatica, 
    boas_vindas, 
    forca_cidade,
    salva_alertas,
    acessa_alertas
)
import json

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY não encontrada no arquivo .env")

client = OpenAI(api_key=api_key)

def formatar_output(texto_saida):
    try:
        dados = json.loads(texto_saida)
        
        print("\n" + "="*50)
        print(f"📍 Cidade: {dados['city']}")
        print(f"⚠️  Nível de Risco: {dados['risk_level']}")
        
        print("\n🔔 Alertas:")
        for alerta in dados['alerts']:
            print(f"  • {alerta}")
            
        print("\n💡 Recomendação:")
        print(f"  {dados['recommendation']}")
        
        print("\n⚡ Ação Necessária:")
        print(f"  {dados['action']}")
        print("="*50 + "\n")
        
        return dados
        
    except json.JSONDecodeError:
        print("\nAnálise da IA:")
        print(texto_saida)
        return None

def menu_principal():
    print("\nEscolha uma opção:")
    print("1. Analisar nova cidade")
    print("2. Ver alertas salvos")
    print("3. Sair")
    
    while True:
        try:
            escolha = input("\nDigite o número da opção desejada (1-3): ")
            if escolha in ['1', '2', '3']:
                return escolha
            print("❌ Opção inválida. Por favor, escolha 1, 2 ou 3.")
        except ValueError:
            print("❌ Por favor, digite um número válido.")

def main():
    boas_vindas()
    
    while True:
        opcao = menu_principal()
        
        if opcao == '1':
            try:
                cidade = forca_cidade()
                dados = analise_climatica(cidade)
                prompt = prepara_prompt(dados)

                print("\n🤖 Analisando dados climáticos com IA...")
                completion = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system",
                            "content": "Você é um assistente de IA especializado em previsão de riscos climáticos. Analise os dados meteorológicos e forneça alertas estruturados sobre riscos de chuva e inundações urbanas. Formate sua resposta como um objeto JSON com a seguinte estrutura: {\"city\": \"nome da cidade\", \"risk_level\": \"BAIXO/MÉDIO/ALTO\", \"alerts\": [\"alerta1\", \"alerta2\"], \"recommendation\": \"texto da recomendação\", \"action\": \"texto da ação\"}"
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                dados_alerta = formatar_output(completion.choices[0].message.content)
                if dados_alerta:
                    salva_alertas(cidade, dados_alerta)

            except ValueError as Erro:
                print(f"\n❌ Erro: {Erro}")
                
        elif opcao == '2':
            print("\nEscolha uma opção:")
            print("1. Ver alertas de uma cidade específica")
            print("2. Ver todos os alertas")
            
            while True:
                try:
                    sub_opcao = input("\nDigite o número da opção desejada (1-2): ")
                    if sub_opcao == '1':
                        cidade = forca_cidade()
                        acessa_alertas(cidade)
                        break
                    elif sub_opcao == '2':
                        acessa_alertas()
                        break
                    else:
                        print("❌ Opção inválida. Por favor, escolha 1 ou 2.")
                except ValueError:
                    print("❌ Por favor, digite um número válido.")
                    
        elif opcao == '3':
            print("\nObrigado por usar a PluvIA! Até logo! 👋")
            break

if __name__ == "__main__":
    main()


#Output Esperado
""" 
{
    "city": "São Paulo",
    "risk_level": "LOW",
    "alerts": [
        "Current weather shows mist with humidity at 82% and cloud coverage at 75%.",
        "No rain recorded in the last hour, but humidity is high."
    ],
    "recommendation": "Monitor conditions closely for sudden changes in humidity or pressure.",
    "action": "Continue regular monitoring of weather updates; no immediate action needed."
}

"""