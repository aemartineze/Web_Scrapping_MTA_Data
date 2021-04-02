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


# uniendo los dataframe en uno
df_mta = pd.concat([ene_2020_clean, feb_2020_clean, mar_2020_clean, abr_2020_clean,
                               may_2020_clean, jun_2020_clean, jul_2020_clean, ago_2020_clean,
                               sep_2020_clean, oct_2020_clean, nov_2020_clean, dic_2020_clean,
                               ene_2021_clean, feb_2021_clean, mar_2021_clean],ignore_index=True)

#Creamos una columna con el indicativo de cada torniquete    
df_mta['Id_Torniquete'] = df_mta['C/A'] + '-' + df_mta['UNIT'] + '-' + df_mta['SCP']    

#Unimos en una sola columna la fecha y la hora
df_mta['Fecha'] =  df_mta['DATE'] + " " + df_mta['TIME']
df_mta.Fecha = pd.to_datetime(df_mta.Fecha)

#Conservamos solo los valores Register de la columna DESC
df_mta = df_mta[df_mta.DESC != 'RECOVR AUD']
    
#Eliminamos las columnas que no son necesarias
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

#Eliminamos las columnas que no son necesarias
frame_primera_hora.drop(['DATE'], axis=1, inplace=True)

###########Edicion Richard: hasta ahi esta el data frame "frame_primera_hora" las primeras fechas 

#Escogemos el registro de cada día solo con la hora más temprana
df_mta_ordenado = df_mta.sort_values(['Id_Torniquete', 'Fecha'])
df_mta_ordenado = df_mta_ordenado.reset_index(drop = True)

#Agrupamos por torniquete
df_mta_aggr = df_mta_ordenado.groupby(['Id_Torniquete'])

#Creamos una columna con el calculo de las entradas mensuales
df_mta_ordenado['Entradas_Tor'] = df_mta_aggr['ENTRIES'].transform(pd.Series.diff)

# guardado el dataset en uno
path = input("Ingrese el path para guardar el archivo ejemplo C:/Users/richa/Google Drive/TIPOLOGÍA Y CICLO DE VIDA DE LOS DATOS/PRACTICA 1 ")
df_mta_ordenado.to_excel(path + '/df_mta.xlsx', header=True, index=False)
