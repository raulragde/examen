import requests as req

URL = 'https://gist.githubusercontent.com/javierIA/06da309a089278be218daf66e02875ab/raw/d0bfabd94c27ad954cba63683d04d460660387f8/salarios.csv'
response = req.get(URL)

if response.status_code == 200:
    print(response.text)
else:
    print("Error al descargar el archivo.")


---------------------------------------------------

import pandas as pd

# Cargar los datos en la variable df
df = pd.read_csv('salarios.csv')

# Verificar que los datos se hayan cargado correctamente
print(df)

------------------------------------------------

import pandas as pd

# Cargar los datos en el DataFrame df
df = pd.read_csv('salarios.csv')

# Mostrar las primeras 5 filas del DataFrame
print(df.head())

0-----------------------------------------

import pandas as pd

# Cargar los datos en el DataFrame df
df = pd.read_csv('salarios.csv')

# Mostrar estadísticas básicas del DataFrame
print(df.describe())
----------------------------------------------

import pandas as pd

# Cargar los datos en el DataFrame df
df = pd.read_csv('salarios.csv')

# Filtrar y seleccionar los datos de la columna "Periodo" mayores a 2018
filtro_periodo = df['Periodo'] > 2018
datos_filtrados = df[filtro_periodo]

# Mostrar las filas donde el "Periodo" es mayor a 2018
print("\nFilas donde la Periodo es mayor a 2018:")
print(datos_filtrados)


---------------------------------------------------------------------

import pandas as pd

# Cargar los datos en el DataFrame df
df = pd.read_csv('salarios.csv')

# Obtener el nombre actual de la segunda columna (trimestre)
nombre_actual = df.columns[1]

# Asignar los nombres a las columnas
nuevas_columnas = ['Periodo', 'Trimestre' if pd.isna(nombre_actual) else nombre_actual, 'Total', '1_salario_minimo', '2_salario_minimo', '3_salario_minimo', '5_salario_minimo', 'mas_de_5_salario_minimo', 'No_recibe_ingresos', 'No_especificado']
df.columns = nuevas_columnas

# Mostrar las columnas después de la modificación
print("Columnas después de la modificación:")
print(df.columns)

-----------------------------------------------------------------

import pandas as pd

# Cargar los datos en el DataFrame df
df = pd.read_csv('salarios.csv')

# Renombrar la columna "Unnamed: 1" a "Trimestre"
df.rename(columns={'Unnamed: 1': 'Trimestre'}, inplace=True)

# Mostrar las columnas después de la modificación
print("Columnas después de la modificación:")
print(df.columns)

---------------------------------------------------------------

import pandas as pd

# Cargar los datos en el DataFrame df
df = pd.read_csv('salarios.csv')

# Renombrar la columna "Unnamed: 1" a "Trimestre"
df.rename(columns={'Unnamed: 1': 'Trimestre'}, inplace=True)

# Calcular el total de ingresos para cada año y período
total_por_periodo = df.groupby(['Periodo', 'Trimestre'])['Total'].sum()

# Mostrar los totales por año y período
print(total_por_periodo)

---------------------------------------------------------------------

import pandas as pd

# Cargar los datos en el DataFrame df
df = pd.read_csv('salarios.csv')

# Renombrar la columna "Unnamed: 1" a "Trimestre"
df.rename(columns={'Unnamed: 1': 'Trimestre'}, inplace=True)

# Calcular los valores nulos en cada columna
valores_nulos = df.isnull().sum()

# Calcular los porcentajes de valores nulos y ordenarlos de forma descendente
porcentajes_nulos = (valores_nulos / len(df)) * 100
porcentajes_nulos_ordenados = porcentajes_nulos.sort_values(ascending=False)

# Mostrar los porcentajes de valores nulos ordenados de forma descendente
print(porcentajes_nulos_ordenados)


------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos en el DataFrame df
df = pd.read_csv('salarios.csv')

# Renombrar la columna "Unnamed: 1" a "Trimestre"
df.rename(columns={'Unnamed: 1': 'Trimestre'}, inplace=True)

# Calcular el total de ingresos para cada período
total_por_periodo = df.groupby('Periodo')['Total'].sum()

# Graficar los ingresos totales por período
plt.figure(figsize=(10, 6))
plt.bar(total_por_periodo.index, total_por_periodo.values)
plt.xlabel('Período')
plt.ylabel('Ingresos Totales')
plt.title('Ingresos Totales por Período')
plt.xticks(total_por_periodo.index)
plt.show()


--------------------------------------------------

import pandas as pd

# Cargar los datos en el DataFrame df
df = pd.read_csv('salarios.csv')

# Renombrar la columna "Unnamed: 1" a "Trimestre"
df.rename(columns={'Unnamed: 1': 'Trimestre'}, inplace=True)

# Definir el tipo de cambio
tipo_cambio = 20

# Función para convertir salario a dólares
def convertir_a_dolares(salario):
    return salario / tipo_cambio

# Aplicar la función de conversión a las columnas deseadas y crear nuevas columnas en dólares
df['Total_dolares'] = df['Total'].apply(convertir_a_dolares)
df['1_salario_minimo_dolares'] = df['1_salario_minimo'].apply(convertir_a_dolares)
df['2_salario_minimo_dolares'] = df['2_salario_minimo'].apply(convertir_a_dolares)
df['3_salario_minimo_dolares'] = df['3_salario_minimo'].apply(convertir_a_dolares)
df['5_salario_minimo_dolares'] = df['5_salario_minimo'].apply(convertir_a_dolares)

# Mostrar el DataFrame con las nuevas columnas en dólares
print(df)


------------------------------------------------------

import pandas as pd
import hashlib

# Cargar los datos en el DataFrame df
df = pd.read_csv('salarios.csv')

# Renombrar la columna "Unnamed: 1" a "Trimestre"
df.rename(columns={'Unnamed: 1': 'Trimestre'}, inplace=True)

# Obtener el DataFrame en formato de cadena
df_string = df.to_string()

# Calcular el hash MD5
md5_hash = hashlib.md5(df_string.encode()).hexdigest()

# Mostrar el token del DataFrame
print("Token del DataFrame:")
print(md5_hash)
