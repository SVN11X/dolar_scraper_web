import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

def run_scraper():
    # URL de ejemplo (puedes cambiarla por la de tu fuente de dólar)
    url = "https://www.bancentral.gov.do/" # Ejemplo genérico

    # Intentar obtener la página y parsearla para usar requests/BeautifulSoup
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        # Ejemplo: usar el título de la página para confirmar que se descargó correctamente
        page_title = soup.title.string.strip() if soup.title and soup.title.string else ""
        # Aquí podrías agregar selectores para extraer el precio real.
        precio_dolar = 58.50  # valor simulado por ahora
    except Exception as e:
        # En caso de fallo de red o parsing, mantener un valor por defecto y registrar la advertencia
        page_title = ""
        precio_dolar = 58.50
        print(f"Advertencia: no se pudo obtener datos de {url}: {e}")

    datos = {
        "precio": precio_dolar,
        "ultima_actualizacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "moneda": "USD",
        "fuente": url,
        "pagina_titulo": page_title
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