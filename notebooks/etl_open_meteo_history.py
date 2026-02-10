import requests
import pandas as pd
import time
import os

def fetch_open_meteo_history(lat, lon, city_name, start_date="2013-01-01", end_date="2024-12-31"):
    """
    Baixa histórico de 12 anos da Open-Meteo (Archive API).
    """
    base_url = "https://archive-api.open-meteo.com/v1/archive"
    
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "daily": ["temperature_2m_mean", "temperature_2m_max", "temperature_2m_min", 
                  "precipitation_sum", "et0_fao_evapotranspiration", "wind_speed_10m_max"],
        "timezone": "America/Sao_Paulo"
    }
    
    print(f"⏳ Baixando dados históricos para {city_name} ({start_date} a {end_date})...")
    
    try:
        response = requests.get(base_url, params=params, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extraindo dados diários
            daily_data = data["daily"]
            df = pd.DataFrame(daily_data)
            
            # Adicionando metadados
            df["municipio"] = city_name
            
            # Renomeando colunas para facilitar depois
            df.rename(columns={
                "time": "data",
                "temperature_2m_mean": "temp_media",
                "temperature_2m_max": "temp_max",
                "temperature_2m_min": "temp_min",
                "precipitation_sum": "precipitacao",
                "et0_fao_evapotranspiration": "evapotranspiracao", # Ótimo que a API já dá isso!
                "wind_speed_10m_max": "vento_max"
            }, inplace=True)
            
            # Salvando
            os.makedirs('data/raw/climate', exist_ok=True)
            filename = f"data/raw/climate/open_meteo_history_{city_name.lower()}.csv"
            df.to_csv(filename, index=False)
            
            print(f"✅ Sucesso! {len(df)} registros salvos em: {filename}")
            return df
            
        else:
            print(f"❌ Erro {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")

# --- Execução para as duas cidades ---
if __name__ == "__main__":
    # Coordenadas aproximadas (Centróides)
    CITIES = {
        "Petrolina": (-9.3986, -40.5079),
        "Juazeiro": (-9.4135, -40.5037)
    }
    
    for city, (lat, lon) in CITIES.items():
        fetch_open_meteo_history(lat, lon, city)
        time.sleep(2) # Pausa amigável para a API