"""
Este archivo pertenece a la capa de infraestructura.
Se encarga de realizar la petición HTTP a la página principal
de La Silla Vacía y retornar el HTML como texto plano.
"""

import requests
from app.utils.constants import NewsConfig


# Obtener el html de la página principal de La Silla Vacía
def fetch_silla_vacia():
    response = requests.get(NewsConfig.LA_SILLA_VACIA_URL)
    if response.status_code != 200:
        #Registrar el error en un log o manejarlo de alguna manera
        return ""
    
    return response.text # Se retorna solo el HTML, no el objeto Response, para mantener el aislamiento de responsabilidades entre capas
