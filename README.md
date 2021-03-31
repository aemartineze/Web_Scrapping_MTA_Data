# Web_Scrapping_MTA_Data
Realizar el web Scrapping de la información de los torniquetes administrados por la MTA (Metropolitan Transportation Authority)
## Contexto
La información ha sido recolectada desde la página web http://web.mta.info/developers/turnstile.html donde existen archivos .txt semanales con la información de los valores registrados de ingresos y salidas en los torniquetes administrados por la MTA dentro de la zona de la ciudad de Nueva York a través de Long Island, sureste del estado de Nueva York y Connecticut. El organismo que publica la información es la MTA por lo cual se dispone de información oficial.
## Título para el dataset
Flujo_personas_torniquetes_MTA
## Descripción del dataset
En el data set se dispondra de la información de los torniquetes y se analizará el movimiento de las personas dentro de la red de transporte.
## Contenido
La descripción de los campos según la MTA se encuentra en la web:
http://web.mta.info/developers/resources/nyct/turnstile/ts_Field_Description.txt
Se disponen de 11 campos: C/A,UNIT,SCP,STATION,LINENAME,DIVISION,DATE,TIME,DESC,ENTRIES,EXITS los cuales se detallan a continuación:
C/A      = Área de Control
UNIT     = Unidad remota para la estación
SCP      = Posición del canal que representa la dirección específica del dispositivo
STATION  = Nombre de la estación
LINENAME = Líneas que llevan a la estación
DIVISION = Línea original de la estación
DATE     = Fecha (MM-DD-YY)
TIME     = Hora (hh:mm:ss) para el evento de auditoría programado
DESc     = Descripción del evento de auditoría 
ENTRIES  = Registro acumulativo de entradas
EXIST    = Registro acumulativo de salidas

La información se encuentra disponible desde el 25 de mayo del 2010 hasta el 27 de marzo de 2021 en archivos semanales almancenados en un link individual a un archivo .txt

Para efectos de este trabajo se tomará la información mensual desde el año 2020 para analizar el efecto de la pandemia COVID-19 en los viajes realizados. 
Se tomarán los archivos de la última semana del mes para calcular el número de pasajeros mensuales en cada estación
