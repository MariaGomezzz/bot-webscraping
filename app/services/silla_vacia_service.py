"""
Este servicio forma parte de la capa de lógica de negocio.
Se encarga de procesar el HTML de La Silla Vacía, ya obtenido por la infraestructura,
y extraer noticias principales y secundarias utilizando BeautifulSoup.
"""
from app.infrastructure.api_la_silla_vacia import fetch_silla_vacia
from app.core.models import NewsFormat
from bs4 import BeautifulSoup

class silla_vacia_service:
  """
  Retorna la noticia principal de La Silla Vacía.
  Extrae el título y el enlace desde el HTML procesado.
  """
  @staticmethod
  def get_news():
    data = fetch_silla_vacia()
    soup = BeautifulSoup(data, 'lxml')

    #Obtener la noticia principal
    news = soup.find("div", class_="entry-wrapper")
    info_news = news.find("h2", class_="entry-title")
    
    #obtener el título y el enlace de la noticia
    title_news = info_news.string.strip()
    link_news = info_news.find("a")["href"] 

    #Una forma de retornar la noticia en un diccionario, pero es mejor usar un modelo (app/core/models) de datos
    # Esto permite mantener la consistencia con el modelo de datos utilizado en la aplicación
    # return {
    #     "title": title_news,
    #     "link": link_news
    # }

    # Imprimir la noticia principal en consola
    # Esto es útil para verificar que se está obteniendo la noticia correctamente
    # Borra el print si no es necesario
    print("------ noticia principal ------")
    print({
        "title": title_news,
        "link": link_news
    })  

    # Usar el modelo NewsFormat para crear una instancia de la noticia
    # Esto permite mantener la consistencia con el modelo de datos utilizado en la aplicación

    return NewsFormat(
        title=title_news,
        link=link_news
    )


  """
  Retorna una lista con todas las noticias de La Silla Vacía.
  Cada noticia incluye título y enlace.
  
  Este método no logra extraer todas las noticias desde La Silla Vacía, debido a que la estructura 
  del HTML no es uniforme y algunas noticias no pueden ser localizadas utilizando esta lógica. 
  Se conserva como referencia para futuros casos en los que se necesite extraer múltiples elementos 
  similares desde un mismo documento HTML.
  """
  @staticmethod
  def get_all_news():
    data = fetch_silla_vacia()
    soup = BeautifulSoup(data, 'lxml')

    #Obtener todas las noticias
    news_list = soup.find_all("div", class_="entry-wrapper")
    all_news = []

    for news in news_list:
      info_news = news.find("h2", class_="entry-title")
      title_news = info_news.string.strip()
      link_news = info_news.find("a")["href"]
      
      #Una forma de gargar las noticias en un diccionario, pero es mejor usar un modelo de datos
      # Esto permite mantener la consistencia con el modelo de datos utilizado en la aplicación
      # all_news.append({
      #     "title": title_news,
      #     "link": link_news
      # })

      # Usar el modelo NewsFormat para crear una instancia de la noticia
      # Esto permite mantener la consistencia con el modelo de datos utilizado en la aplicación    
      all_news.append(NewsFormat(
          title=title_news,
          link=link_news
      ))

      # Imprimir todas las noticias en consola
      # Esto es útil para verificar que se están obteniendo las noticias correctamente  
      # Borra el print si no es necesario
      print("------ todas las noticias ------")
      for new in all_news:
          print({
              "title": new.title,
              "link": new.link
          })

    return all_news

