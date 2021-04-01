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

mar_2021 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[40])
feb_2021 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[44])
ene_2021 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[49])
dic_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[53])
nov_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[57])
oct_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[62])
sep_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[66])
ago_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[70])
jul_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[75])
jun_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[79])
may_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[84])
abr_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[88])
mar_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[92])
feb_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[96])
ene_2020 = pd.read_csv('http://web.mta.info/developers/'+ lista_txt[101])

# limpiando los meses solo tomando el primer día de cada mes
posic_01 = mar_2021.loc[:,'DATE'] == '03/01/2021'
mar_2021_clean = mar_2021.loc[posic_01]

posic_01 = feb_2021.loc[:,'DATE'] == '02/01/2021'
feb_2021_clean = feb_2021.loc[posic_01]

posic_01 = ene_2021.loc[:,'DATE'] == '01/01/2021'
ene_2021_clean = ene_2021.loc[posic_01]

posic_01 = dic_2020.loc[:,'DATE'] == '12/01/2020'
dic_2020_clean = dic_2020.loc[posic_01]

posic_01 = nov_2020.loc[:,'DATE'] == '11/01/2020'
nov_2020_clean = nov_2020.loc[posic_01]

posic_01 = oct_2020.loc[:,'DATE'] == '10/01/2020'
oct_2020_clean = oct_2020.loc[posic_01]

posic_01 = sep_2020.loc[:,'DATE'] == '09/01/2020'
sep_2020_clean = sep_2020.loc[posic_01]

posic_01 = ago_2020.loc[:,'DATE'] == '08/01/2020'
ago_2020_clean = ago_2020.loc[posic_01]

posic_01 = jul_2020.loc[:,'DATE'] == '07/01/2020'
jul_2020_clean = jul_2020.loc[posic_01]

posic_01 = jun_2020.loc[:,'DATE'] == '06/01/2020'
jun_2020_clean = jun_2020.loc[posic_01]

posic_01 = may_2020.loc[:,'DATE'] == '05/01/2020'
may_2020_clean = may_2020.loc[posic_01]

posic_01 = abr_2020.loc[:,'DATE'] == '04/01/2020'
abr_2020_clean = abr_2020.loc[posic_01]

posic_01 = mar_2020.loc[:,'DATE'] == '03/01/2020'
mar_2020_clean = mar_2020.loc[posic_01]

posic_01 = feb_2020.loc[:,'DATE'] == '02/01/2020'
feb_2020_clean = feb_2020.loc[posic_01]

posic_01 = ene_2020.loc[:,'DATE'] == '01/01/2020'
ene_2020_clean = ene_2020.loc[posic_01]

vuelos = pd.concat([ene_2020_clean, feb_2020_clean, mar_2020_clean, abr_2020_clean,
                               may_2020_clean, jun_2020_clean, jul_2020_clean, ago_2020_clean,
                               sep_2020_clean, oct_2020_clean, nov_2020_clean, dic_2020_clean,
                               ene_2021_clean, feb_2021_clean, mar_2021_clean],ignore_index=True)

# uniendo los dataframe en uno
vuelos = pd.concat([ene_2020_clean, feb_2020_clean, mar_2020_clean, abr_2020_clean,
                               may_2020_clean, jun_2020_clean, jul_2020_clean, ago_2020_clean,
                               sep_2020_clean, oct_2020_clean, nov_2020_clean, dic_2020_clean,
                               ene_2021_clean, feb_2021_clean, mar_2021_clean],ignore_index=True)

# guardado el dataset en uno
path = input("Ingrese el path para guardar el archivo ejemplo C:/Users/richa/Google Drive/TIPOLOGÍA Y CICLO DE VIDA DE LOS DATOS/PRACTICA 1 ")
vuelos.to_excel(path + '/vuelos.xlsx', header=True, index=False)