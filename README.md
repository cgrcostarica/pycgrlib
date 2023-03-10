# pycgrlib
Libreria de funciones para uso de herramientas en la Contraloria General de la Republica (CGR)

## Cómo instalar la libreria?

```
git clone https://github.com/cgrcr/pycgrlib.git
cd pycgrlib
python -m build
pip install .
```

## Documentación 

### generador_datos

| Nombre función | Descripción | 
|----------------|-------------|
| nombres_masculinos| Listado de nombres masculinos|
| nombres_femeninos| Listado de nombres femeninos|
| apellidos | Listado de apellidos|
| get_provincias() | Devuelve una lista con el nombre de las provincias de Costa Rica | get_provincias() |
| get_cantones() | Devuelve una lista con el nombre de los cantones de Costa Rica, recibiendo como parámetro el nombre de la provincia  | 
| get_distritos(p_provincia, p_canton) | Devuelve una lista con el nombre de los distritos de Costa Rica, recibiendo como parámetro el nombre de la provincia y el cantón  |
| imprimir_estadisticas_listas() | Imprime el número de elementos en las listas de nombres masculinos, nombres femeninos y apellidos.|
| generar_nombre(sexo=None, nombre_compuesto=False) | Esta función genera un nombre aleatorio a partir de dos listas de nombres y apellidos. El parámetro sexo es opcional y puede ser "m" para masculino o "f" para femenino. El parámetro nombre_compuesto indica si el nombre generado será compuesto o no. Si el parámetro sexo no se especifica, la función generará un nombre aleatorio de cualquier sexo con o sin nombre compuesto.|
| generar_cedula() | Esta función genera un número de cédula aleatorio para una persona en Costa Rica. La cédula está formada por 3 partes: una provincia (1 a 8), un número (0 a 1600 o 0 a 999) y un número (0 a 9999).|
| generar_telefono()| Devuelve un numero de telefono generado aleatoreamente, si el tipo es 'c' es celular, y 'f' es telefono fijo|
| generar_provincia()| Devuelve una provincia aleatoria de la lista de provincias disponibles|
| generar_canton()| Devuelve un cantón aleatorio de la lista de cantones disponibles|
| generar_distrito()| Devuelve un distrito aleatorio de la lista de distritos disponibles|
| generar_coordinada()| Devuelve un coordenada de la lista de coordinadas disponibles |
| generar_direccion() | Devuelve una dirección aleatoria en formato de texto utilizando funciones auxiliares generar_coordinada, generar_provincia, generar_canton y generar_distrito. La dirección generada incluye la cantidad de metros en bloques de 100 de la ubicación, la coordenada de la ubicación (Norte, Sur, Este, Oeste), el tipo de lugar (elegido de la lista lugares), el nombre del lugar (elegido de la lista nombre_lugares), el distrito, el cantón y la provincia. Puede recibir la provincia y canton para generar la dirección.|
| generar_salario() | Devuelve un salario aleatorio entre 330,000 y 2,500,000 colones|
| generar_persona() | Devuelve una lista de datos aleatorios para una persona especificada por la cantidad en el parámetro "p_cantidad". La información generada incluye un nombre, un número de cédula, una dirección, una provincia, un cantón, un distrito, un salario y un número de teléfono. También se proporciona un género opcional "p_sexo" para la generación del nombre. La función devuelve la lista completa de información generada para cada persona.|

# Ejemplo de uso

```
from pycgrlib import generador_datos as gd 
import pandas as pd

personas = gd.generar_persona(50)
data = pd.DataFrame(personas, columns=gd.columnas)
data.to_csv("salida.csv",sep="|", encoding='UTF-8', index=False)
```

## Changelog

Puede ver el registro completo de cambios en el archivo [CHANGELOG.md](CHANGELOG.md)
