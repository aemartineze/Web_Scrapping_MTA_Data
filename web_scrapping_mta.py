# -*- coding: utf-8 -*-

#Importamos las librerias necesarias
from bs4 import BeautifulSoup
import requests
import pandas as pd



#Dirección web de "The Metropolitan Transportation Authority" con las estadísticas de los pasajeros que pasan por los torniquetes del metro de NYC
dir_web = "http://web.mta.info/developers/turnstile.html" 

#Utilizamos la libreria BeautifulSoup para acceder a la información 
page = requests.get(dir_web)
soup = BeautifulSoup(page.text, "html.parser")

#Visualizamos todas las referencias de objetos en la página que en este caso son los archivos txt
#Guardamos en una lista
lista_txt =[]
for link in soup.find_all("a"):
    lista_txt.append(link.get('href'))

#Vamos a trabajar unicamente con la data desde el 2020
#Ejemplo semana del 26 de diciembre de 2020
    
download_dir = 'http://web.mta.info/developers/'+ lista_txt[50]
data = pd.read_csv(download_dir)