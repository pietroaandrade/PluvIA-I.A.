# PluvIA - Sistema de Análise de Riscos Climáticos

O PluvIA é um sistema inteligente que combina dados meteorológicos em tempo real com inteligência artificial para prever e alertar sobre riscos de chuva e inundações em grandes cidades brasileiras.

###
<h1 align="left">Integrantes</h1>

###

<h3 align="left">Ícaro Henrique de Souza Calixto - RM560278</h3>

###

<h3 align="left">Pietro Brandalise De Andrade - RM560142</h3>

###

## Funcionalidades

- Análise em tempo real de condições climáticas
- Previsão de riscos de chuva e inundações
- Monitoramento de 10 grandes cidades brasileiras
- Sistema de alertas com níveis de risco
- Histórico de alertas por cidade
- Interface amigável em português

## Requisitos

- Python 3.8 ou superior
- Conta na OpenAI (para API key)
- Conta no OpenWeather (para API key)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/pluvia.git
cd pluvia
```

2. Crie e ative um ambiente virtual:
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione suas chaves de API:
```env
OPENAI_API_KEY=sua_chave_da_openai
OPENWEATHER_API_KEY=sua_chave_do_openweather
```

## Obtendo as Chaves de API

### OpenAI API Key
1. Acesse [OpenAI Platform](https://platform.openai.com/api-keys)
2. Faça login ou crie uma conta
3. Vá para "API Keys"
4. Clique em "Create new secret key"
5. Copie a chave gerada

### OpenWeather API Key
1. Acesse [OpenWeather](https://openweathermap.org/api)
2. Crie uma conta gratuita
3. Vá para "My API Keys"
4. Copie sua chave de API

## Como Usar

1. Ative o ambiente virtual (se ainda não estiver ativo):
```bash
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate     # Windows
```

2. Execute o programa:
```bash
python main.py
```

3. Siga o menu interativo no terminal...
   

## Estrutura do Projeto

```
pluvia/
├── main.py              # Interface principal e lógica do programa
├── weatherAnalysis.py   # Análise de dados climáticos
├── openweather.py       # Integração com API do OpenWeather
├── prompt.py           # Template para análise meteorológica
├── requirements.txt    # Dependências do projeto
├── .env               # Configurações de ambiente (não versionado)
└── alertas.json       # Histórico de alertas (gerado automaticamente)
```

## Níveis de Risco

- **BAIXO**: Condições normais, sem alertas
- **MÉDIO**: Atenção necessária, monitoramento
- **ALTO**: Risco significativo, ações preventivas
- **SEVERO**: Risco iminente, ações imediatas necessárias

## Solução de Problemas

1. **Erro de API Key não encontrada**
   - Verifique se o arquivo `.env` existe
   - Confirme se as chaves estão corretamente formatadas
   - Certifique-se de que o arquivo está na raiz do projeto

2. **Erro de módulos não encontrados**
   - Verifique se o ambiente virtual está ativo
   - Execute `pip install -r requirements.txt` novamente

3. **Erro de conexão com API**
   - Verifique sua conexão com a internet
   - Confirme se as chaves de API são válidas
   - Aguarde alguns minutos e tente novamente







Para sugestões, dúvidas ou problemas, abra uma issue no GitHub ou entre em contato através do email: seu-email@exemplo.com
