import requests
import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo   # Python 3.9+

def run_scraper():
    # API oficial de indicadores económicos de Chile (mindicador.cl)
    api_url = "https://mindicador.cl/api/dolar"

    try:
        resp = requests.get(api_url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        # Extraer el valor del dólar observado (en pesos chilenos)
        precio_dolar = data.get("serie", [{}])[0].get("valor")
        if precio_dolar is None:
            raise ValueError("No se encontró el valor del dólar en la respuesta de mindicador.")

        # Redondear a 2 decimales (opcional)
        precio_dolar = round(float(precio_dolar), 2)

    except Exception as e:
        print(f"ERROR: No se pudo obtener el precio del dólar desde {api_url}: {e}")
        return  # Salir sin guardar datos corruptos

    # Obtener la hora actual en la zona horaria de Chile (Santiago)
    chile_tz = ZoneInfo("America/Santiago")
    ahora_chile = datetime.now(chile_tz)
    ultima_actualizacion = ahora_chile.strftime("%Y-%m-%d %H:%M:%S")

    datos = {
        "precio": precio_dolar,
        "ultima_actualizacion": ultima_actualizacion,
        "moneda": "CLP",
        "fuente": "mindicador.cl (dólar observado)"
    }

    os.makedirs('data', exist_ok=True)
    ruta_archivo = os.path.join("data", "precios.json")
    with open(ruta_archivo, "w", encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print(f"Datos guardados exitosamente: {datos}")

if __name__ == "__main__":
    run_scraper()