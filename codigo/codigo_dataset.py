# Importamos las librerias necesarias
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime, timedelta
import time


# Dirección web de "The Metropolitan Transportation Authority" con las estadísticas de los pasajeros que pasan por los torniquetes del metro de NYC
dir_web = "http://web.mta.info/developers/turnstile.html" 

# Utilizamos la libreria BeautifulSoup para acceder a la información 
page = requests.get(dir_web)
soup = BeautifulSoup(page.text, "html.parser")

# Visualizamos todas las referencias de objetos en la página que en este caso son los archivos txt
# Guardamos en una lista
lista_txt =[]
for link in soup.find_all("a"):
    lista_txt.append(link.get('href'))
    
# Eliminamos valores nulos    
lista_txt = [x for x in lista_txt if x]

# Filtramos los links de fechas
lista_txt = [x for x in lista_txt if 'turnstile_' in x]

# Generamos la lista con los links 
lista_txt = ['http://web.mta.info/developers/'+x for x in lista_txt]


# Establecemos un rango de fecha para leer los archivos
fecha_inicial = datetime(2019,1,1)   
fecha_final = datetime(2021,3,31)
rango_fechas = [(fecha_inicial + timedelta(days=d))
                    for d in range((fecha_final - fecha_inicial).days + 1)] 

# Filtramos solo los sábados
rango_fechas = [fecha.strftime("%y%m%d") for fecha in rango_fechas if fecha.weekday()  in [5]]

# Filtramos los primeros días de cada mes
s = pd.Series(pd.to_datetime(rango_fechas, format="%y%m%d"))
rango_fechas = s.groupby(s.dt.strftime('%y%m')).min().tolist()
rango_fechas = [dt.strftime('%y%m%d') for dt in rango_fechas]


# Filtrar la lista_txt_ en funcion del rango_fechas
lista_txt_final = [x for x in lista_txt if any(substring in x for substring in rango_fechas)]
    
df_mta = pd.DataFrame()
for fecha in lista_txt_final:
    aux = pd.read_csv(fecha)
    time.sleep(2)
    df_mta = pd.concat([df_mta,aux],ignore_index=True)

# Creamos una columna con el indicativo de cada torniquete    
df_mta['Id_Torniquete'] = df_mta['C/A'] + '-' + df_mta['UNIT'] + '-' + df_mta['SCP']    

# Unimos en una sola columna la fecha y la hora
df_mta['Fecha'] =  df_mta['DATE'] + " " + df_mta['TIME']
df_mta.Fecha = pd.to_datetime(df_mta.Fecha)

# limpiando los meses solo tomando el primer día de cada mes
df_mta = df_mta.loc[df_mta['Fecha'].dt.day == 1]


# Conservamos solo los valores Register de la columna DESC
df_mta = df_mta[df_mta.DESC != 'RECOVR AUD']
    
# Eliminamos las columnas que no son necesarias
df_mta.drop(['C/A', 'UNIT','SCP','TIME'], axis=1, inplace=True)

# creando dataframe para guardar lo limpio
frame_primera_hora = pd.DataFrame()
for i in df_mta.Id_Torniquete.unique():  # recorro cada Id unico
    torniquete = df_mta.loc[:,'Id_Torniquete'] == i
    torniquete_cl = df_mta.loc[torniquete]  # creo nuevo dataframe solo un torniquete id unico
    for j in df_mta.DATE.unique():  # recorro cada una de las 14 fechas (strings)
        fecha_torniquete = torniquete_cl.loc[:,'DATE'] == j
        fecha_torniquete_cl = torniquete_cl.loc[fecha_torniquete]
        try:  # cuando no hay dato en esa instancia de fecha
            fecha_corta = fecha_torniquete_cl.loc[:,'Fecha'] == min(fecha_torniquete_cl.Fecha)
            final = fecha_torniquete_cl.loc[fecha_corta]
        except ValueError:
            continue
        # concateno cada dataframe que voy sacando
        frame_primera_hora = frame_primera_hora.append(final, ignore_index=True)

# Eliminamos las columnas que no son necesarias
frame_primera_hora.drop(['DATE', 'DESC'], axis=1, inplace=True)

# Cambiamos los nombres de las columnas
Registros_torniquetes_MTA = frame_primera_hora
Registros_torniquetes_MTA.columns=['Estacion','Linea','Division', 'Entradas', 'Salidas', 'Id_Torniquete', 'Fecha'] 

# Cambiamos el orden de las columnas
Registros_torniquetes_MTA = Registros_torniquetes_MTA[['Id_Torniquete', 'Fecha', 'Estacion','Linea','Division','Entradas', 'Salidas']]

# Preguntamos un path para guardar el dataset generado
path = input("Ingrese el path para guardar el archivo ejemplo C:/Users/richa/Google Drive/TIPOLOGÍA Y CICLO DE VIDA DE LOS DATOS/PRACTICA 1 ")
Registros_torniquetes_MTA.to_csv(path + '/Registros_torniquetes_MTA.csv', header=True, index=False)
