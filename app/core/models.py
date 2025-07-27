"""
Este archivo contiene la definición del modelo de datos para las noticias.
Utiliza Pydantic para validar y estructurar los datos de las noticias.

En otras palabras, es la estructura que se utilizará para retornar las noticias
extraídas de La Silla Vacía.

Se utiliza en el servicio `silla_vacia_service` para retornar las noticias
de forma consistente y validada.
"""

from pydantic import BaseModel

class NewsFormat(BaseModel):
    title: str
    link: str
