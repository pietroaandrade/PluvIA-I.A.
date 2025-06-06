from openweather import getWeather
from prompt import WeatherPredictionPrompt
import json
from datetime import datetime

cities = {
    "São Paulo": {"lat": "-23.5475", "lon": "-46.63611"},
    "Rio de Janeiro": {"lat": "-22.9068", "lon": "-43.1729"},
    "Belo Horizonte": {"lat": "-19.9167", "lon": "-43.9345"},
    "Salvador": {"lat": "-12.9714", "lon": "-38.5014"},
    "Brasília": {"lat": "-15.7801", "lon": "-47.9292"},
    "Curitiba": {"lat": "-25.4284", "lon": "-49.2733"},
    "Recife": {"lat": "-8.0476", "lon": "-34.8770"},
    "Porto Alegre": {"lat": "-30.0346", "lon": "-51.2177"},
    "Fortaleza": {"lat": "-3.7319", "lon": "-38.5267"},
    "Manaus": {"lat": "-3.1190", "lon": "-60.0217"}
}


alertas_salvos = {}

def indice_cidade(cidades):
    return {str(i+1): cidade for i, cidade in enumerate(cidades.keys())}

def boas_vindas():
    print("\n🌧️  Bem-vindo a PluvIA - Sistema de Análise de Riscos Climáticos 🌧️")
    print("__"*50)
    print("\nEste sistema analisa dados meteorológicos e fornece previsões")
    print("de riscos de chuva e inundações em grandes cidades brasileiras.\n")

def exibir_cidades():
    print("\nCidades disponíveis:")
    indices = indice_cidade(cities)
    for indice, cidade in indices.items():
        print(f"{indice}. {cidade}")

def forca_cidade():
    while True:
        try:
            exibir_cidades()
            indices = indice_cidade(cities)
            escolha = input("\nPor favor, selecione o número da cidade (1-10): ")
            
            if escolha in indices:
                return indices[escolha]
            else:
                print("\n❌ Escolha inválida. Por favor, selecione um número entre 1 e 10.")
        except ValueError:
            print("\n❌ Por favor, digite um número válido.")

def analise_climatica(cidade):
    print(f"\n🔍 Obtendo dados climáticos para {cidade}...")
    lat = cities[cidade]["lat"]
    lon = cities[cidade]["lon"]

    dados_climaticos = getWeather(lat, lon)
    if dados_climaticos:
        print("✅ Dados climáticos obtidos com sucesso!")
    return dados_climaticos

def prepara_prompt(dados_climaticos):
    infoPrompt = WeatherPredictionPrompt(dados_climaticos)
    return infoPrompt

def salva_alertas(cidade, dados_alerta):

    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if cidade not in alertas_salvos:
            alertas_salvos[cidade] = []
        
        alerta = {
            "timestamp": timestamp,
            "dados": dados_alerta
        }
        alertas_salvos[cidade].append(alerta)
        print(f"\n✅ Alertas para {cidade} salvos com sucesso!")
        
        with open('alertas.json', 'w', encoding='utf-8') as f:
            json.dump(alertas_salvos, f, ensure_ascii=False, indent=4)
            
    except Exception as e:
        print(f"\n❌ Erro ao salvar alertas: {str(e)}")

def acessa_alertas(cidade=None): 
    try:
        
        try:
            with open('alertas.json', 'r', encoding='utf-8') as f:
                alertas_carregados = json.load(f)
                alertas_salvos.update(alertas_carregados)
        except FileNotFoundError:
            pass

        if not alertas_salvos:
            print("\n📭 Nenhum alerta salvo encontrado.")
            return

        if cidade:
            if cidade in alertas_salvos:
                print(f"\n📊 Alertas para {cidade}:")
                for alerta in alertas_salvos[cidade]:
                    print("\n" + "="*50)
                    print(f"📅 Data/Hora: {alerta['timestamp']}")
                    dados = alerta['dados']
                    print(f"⚠️  Nível de Risco: {dados['risk_level']}")
                    print("\n🔔 Alertas:")
                    for alert in dados['alerts']:
                        print(f"  • {alert}")
                    print(f"\n💡 Recomendação: {dados['recommendation']}")
                    print(f"⚡ Ação: {dados['action']}")
            else:
                print(f"\n❌ Nenhum alerta encontrado para {cidade}")
        else:
            print("\n📊 Alertas salvos para todas as cidades:")
            for cidade, alertas in alertas_salvos.items():
                print(f"\n📍 {cidade}:")
                for alerta in alertas:
                    print(f"  • {alerta['timestamp']} - Nível: {alerta['dados']['risk_level']}")

    except Exception as e:
        print(f"\n❌ Erro ao acessar alertas: {str(e)}")