# Web_Scrapping_MTA_Data
Realizar el web Scrapping de la información de los torniquetes administrados por la MTA (Metropolitan Transportation Authority)
## Integrantes del Grupo
 - Richard Jácome Guanoluisa
 - Andrea Martínez Espinosa

Para ejecutar el script es necesario instalar la siguientes librerías:
```
pip install pandas
pip install requests
pip install bs4
pip install datetime
pip install time
```

El script se debe ejecutar de la siguiente manera:
```
python3 codigo_dataset.py
```

Se disponen de 11 campos de acuerdo al siguiente detalle:

* C/A = Área de Control
* UNIT = Unidad remota para la estación
* SCP = Posición del canal que representa la dirección específica del dispositivo
* STATION = Nombre de la estación
* LINENAME = Líneas que llevan a la estación
* DIVISION = Línea original de la estación
* DATE = Fecha (MM-DD-YY)
* TIME = Hora (hh:mm:ss) para el evento de auditoría programado
* DESC = Descripción del evento de auditoría
* ENTRIES = Registro acumulativo de entradas
* EXIST = Registro acumulativo de salidas

La información se encuentra disponible desde el 25 de mayo del 2010 hasta el 03 de abril de 2021 en archivos semanales almacenados en un enlace individual a un archivo .txt.
Para efectos de este trabajo se tomará la información mensual desde el año 2019 para analizar el efecto de la pandemia COVID-19 en los viajes realizados. Se tomará la información del primer día del mes para calcular el número de pasajeros mensuales en cada estación.
Para efectos de esta práctica se depuró la información de las columnas por lo que el dataset resultante Registros_torniquetes_MTA tiene los siguientes registros:

* Id_Torniquete = Id único del torniquete (se compone de los campos originales C/A, UNIT, SCP)
* Fecha = Fecha y hora (AAAA-MM-DD hh:mm:ss)
* Estacion = Nombre de la estación
* Linea = Líneas que llevan a la estación
* Division = Línea original de la estación
* Entradas = Registro acumulativo de entradas
* Salidas = Registro acumulativo de salidas


## Archivos
 - codigo/codigo_dataset.py: archivo con código para generar el dataset
 - PRA1_web_scrapping_mta.pdf: repuestas a la práctica
 - Registros_torniquetes_MTA.csv: dataset resultante
