import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    raise ValueError("OPENWEATHER_API_KEY não encontrada no arquivo .env")


def getWeather(lat, lon, api_key=api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    max_tentativas = 3
    tempo_espera = 2  

    for tentativa in range(max_tentativas):
        try:
            print(f"Tentando obter dados climáticos (tentativa {tentativa + 1}/{max_tentativas})...")
            r = requests.get(url)
            r.raise_for_status()
            dados = r.json()
            return dados
            
        except requests.exceptions.HTTPError as erro_http:
            if r.status_code == 401:
                print("❌ Falha na autenticação. Por favor, verifique sua chave de API.")
                raise ValueError("Chave de API inválida")
            elif r.status_code == 404:
                print("❌ Dados climáticos não encontrados para a localização especificada.")
                raise ValueError("Localização não encontrada")
            elif r.status_code == 429:
                print("⚠️ Limite de requisições excedido. Aguardando antes de tentar novamente...")
                time.sleep(tempo_espera)
                continue
            else:
                print(f"❌ Erro HTTP ocorreu: {erro_http}")
                
        except requests.exceptions.RequestException as erro_rede:
            print(f"❌ Erro de rede ocorreu: {erro_rede}")
            if tentativa < max_tentativas - 1:
                print(f"Tentando novamente em {tempo_espera} segundos...")
                time.sleep(tempo_espera)
            continue
            
        except ValueError as erro_json:
            print(f"❌ Erro ao processar dados climáticos: {erro_json}")
            raise ValueError("Dados climáticos inválidos recebidos")
            
    raise ValueError("Falha ao obter dados climáticos após várias tentativas")

#Teste
"""if __name__ == "__main__":
    city = "São Paulo"
    lat = cities[city]["lat"]
    lon = cities[city]["lon"]
    weather_data = getWeather(lat, lon)
    print(weather_data)"""