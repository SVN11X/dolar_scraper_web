import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

def run_scraper():
    # URL de ejemplo (puedes cambiarla por la de tu fuente de dólar)
    url = "https://www.bancentral.gov.do/" # Ejemplo genérico
    
    # --- Lógica de scraping (Simplificada) ---
    # Aquí iría tu lógica con BeautifulSoup. Por ahora, simulamos un dato:
    precio_dolar = 58.50 
    # -----------------------------------------

    datos = {
        "precio": precio_dolar,
        "ultima_actualizacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "moneda": "USD"
    }

    # Asegurarse de que la carpeta 'data' existe
    os.makedirs('data', exist_ok=True)

    # Guardar en data/precios.json
    ruta_archivo = os.path.join("data", "precios.json")
    with open(ruta_archivo, "w", encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    
    print(f"Datos guardados exitosamente: {datos}")

if __name__ == "__main__":
    run_scraper()