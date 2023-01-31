from matplotlib.pyplot import axhline
import pandas as pd
import datetime
import time
import os
import hashlib
import matplotlib.pyplot as plt


class Archivo:
    def __init__(self, ruta, separador=None, columnas=None, dataframe=None):
        try:
            self.ruta = ruta
            self.separador = self.__detectar_separador(separador, dataframe)
            self.fecha_carga = datetime.datetime.now()
            self.datos = self.__cargar_datos(ruta, columnas, dataframe)
            self.datos_originales = self.datos
            self.nombre_columnas = self.datos.columns.tolist()
            if not self.datos.empty:
                print(f"Archivo {ruta} leido correctamente")
            else:
                print(f"Archivo {ruta} se leyó correctamente pero esta vacio")
        except Exception as e:
            print(f"Error al leer el archivo, intente de nuevo {e}")

    def __str__(self) -> str:
        return str(self.datos.head())

    def __detectar_separador(self, sep, dataframe):
        if dataframe is not None:
            return ''

        if sep is None:
            texto = ""
            with open(self.ruta, encoding="latin-1") as archivo:
                for x in range(3):
                    texto += next(archivo).strip()

                comma = texto.count(",")
                punto_comma = texto.count(";")
                pipe = texto.count("|")

                if (comma >= punto_comma) and (comma >= pipe):
                    return ','
                elif (punto_comma >= comma) and (punto_comma >= pipe):
                    return ';'
                else:
                    return '|'
        else:
            return sep

    def __cargar_datos(self, ruta, columnas=None, dataframe=None):

        if dataframe is None:
            self.nombre, self.extension = os.path.splitext(ruta)
            if self.extension == '.csv' or self.extension == '.txt':
                try:
                    data = pd.read_csv(
                        ruta, sep=self.separador, encoding='latin-1')
                    if columnas is not None:
                        data.columns = columnas
                    self.filas = len(data)
                    self.columnas = len(data.columns)
                    return data
                except FileNotFoundError:
                    print("La ruta del archivo no es valida")
                    return None
            if self.extension == '.xls':
                try:
                    data = pd.read_excel(ruta)
                    self.filas = len(data)
                    self.columnas = len(data.columns)
                    return data
                except FileNotFoundError:
                    print("La ruta del archivo no es valida")
                    return None
        else:
            self.datos = dataframe
            return dataframe

    def cargar_dataframe(self, df):
        self.datos = df
        return df

    def extraer_muestra(self, porcentaje=None, cantidad=None):
        if cantidad and porcentaje:
            print("Solamente debe seleccionar un parametro, porcentaje o cantidad")
            return None
        if cantidad:
            if cantidad > 0:
                cantidad_int = int(cantidad)
                return self.datos.sample(n=cantidad_int)
            else:
                print("El numero debe ser mayor a 0")
                return None
        if porcentaje:
            if (porcentaje <= 1):
                return self.datos.sample(frac=porcentaje)
            else:
                print("El porcentaje debe estar entre 0 y 1")
                return None
        return "Debe proporcionar los parametros requeridos: porcentaje o cantidad"

    def limpiar_espacios(self):
        def trim_strings(x): return x.strip() if isinstance(x, str) else x
        self.datos = self.datos.applymap(trim_strings)

    def inicio(self):
        return self.datos.head()

    def fin(self):
        return self.datos.tail()

    def info(self):
        return self.datos.info()

    def describir(self, columna=None):
        if columna is None:
            return self.datos.describe()
        else:
            return self.datos[columna].describe()

    def eliminar_vacios(self):
        self.datos = self.datos.dropna()

    def graficar(self, columna, tipo, etiqueta_x="", etiqueta_y=""):
        if tipo == 'caja':
            return self.datos[columna].plot(kind='box', vert=False, figsize=(14, 6))
        if tipo == 'densidad':
            return self.datos[columna].plot(kind='density', figsize=(14, 6))
        if tipo == 'densidad_v2':
            ax = self.datos[columna].plot(kind='density', figsize=(14, 6))
            ax.axhline(self.datos[columna].mean(), color='red')
            ax.axhline(self.datos[columna].median(), color='green')
            return ax
        if tipo == 'histograma':
            ax = self.datos[columna].plot(kind='hist', figsize=(14, 6))
            ax.set_ylabel(etiqueta_y)
            ax.set_xlabel(etiqueta_x)
        if tipo == 'categorias_barra':
            return self.datos[columna].value_counts().plot(kind='pie', figsize=(14, 6), autopct='%1.1f%%')
        if tipo == 'barra_vertical':
            return self.datos[columna].plot(kind='bar', figsize=(14, 6))
        if tipo == 'barra_horizontal':
            return self.datos[columna].plot(kind='barh', figsize=(14, 6))

    def matriz_correlacion(self):
        corr = self.datos.corr()
        fig = plt.figure(figsize=(8, 8))
        plt.matshow(corr, cmap='RdBu', fignum=fig.number)
        plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
        plt.yticks(range(len(corr.columns)), corr.columns)

    def categorizar_y_contar(self, columna):
        return self.datos[columna].value_counts()


class Utils:
    # Para leer en pedazos de 64Kb los datos para el hash
    BUF_SIZE = (64 * (1024))

    def guardar_csv(data, separador=";", index=False, nombre=None, encabezados=True):
        if nombre is None:
            nombre_archivo = time.strftime("%Y%m%d-%H%M%S") + ".csv"
        else:
            nombre_archivo = nombre + ".csv"
        data.to_csv(nombre_archivo, sep=separador,
                    index=index, header=encabezados)
        print("El archivo se guardo correctamente en: " + nombre_archivo)

    def hash_sha1(ruta):
        sha1 = hashlib.sha1()

        with open(ruta, 'rb') as f:
            while True:
                data = f.read(Utils.BUF_SIZE)
                if not data:
                    break
                sha1.update(data)

        # return pd.util.hash_pandas_object(data)
        return sha1.hexdigest()

    def calcular_numero_columnas():
        # Esta función lee un archivo csv o txt y calcula el numero de columnas que tiene
        pass

    def verificar_numero_columnas():
        # Esta función lee un archivo csv o txt y verifica si todas las filas tienen la misma cantidad de columnas
        pass

    def crear_dataframe():
        pass

    def agregar_fila_dataframe():
        pass

    def eliminar_duplicados():
        pass

    def eliminar_columna():
        pass

    def reemplazar_strings_dataframe():
        pass

    def imprimir(texto):
        fecha = time.time()
        print(f"{fecha,texto}")
