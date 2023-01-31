import datetime
from colorama import Fore, Style


def imprimir(texto):
        date = datetime.datetime.now().strftime("%x %X")
        salida = f"[{Fore.GREEN}{date}{Style.RESET_ALL}] {texto}"
        print(salida)


def respuesta_json(resultado, mensaje, datos):
    return {"resultado": resultado, "mensaje": mensaje, "datos": datos}


# Funcion que da formato a una cedula
def formatocedula(row,campo_cedula):
    try:
        if len(row[campo_cedula]) == 10:
            if row[campo_cedula][:1] == '0':
                return row[campo_cedula][1:]
            if row[campo_cedula][:1] == '3':
                return "CED_JURI_" + row[campo_cedula]
            else:
                return "OTROS_" + row[campo_cedula]
        if len(row[campo_cedula]) == 9:
            return row[campo_cedula]
        #return 'FORMATO INCORRECTO: ' + str(row[campo_cedula])
        return 'FORMATO INCORRECTO'
    except Exception as ex:
        return str(ex)


# Funcion que da formato a una cedula
def formatocedula2(row):
    try:
        if len(row["CEDULA"]) == 10:
            if row["CEDULA"][:1] == '0':
                return row["CEDULA"][1:]
            if row["CEDULA"][:1] == '3':
                return "CED_J_" + row["CEDULA"][0:]
            else:
                return "OTROS_" + + row["CEDULA"][1:]
        if len(row["CEDULA"]) == 9:
            return row["CEDULA"]
        return 'FORMATO INCORRECTO'
    except:
        return 'FORMATO INCORRECTO'