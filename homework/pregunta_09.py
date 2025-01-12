"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    with open("files/input/data.csv", "r") as files:
        lines = files.readlines()
    lista = [elem.strip().split("\t")[4].split(",") for elem in lines]

    conteo_claves = {}

    for sublista in lista:
        for par in sublista:
            clave, valor = par.split(":")
            # Incrementar el conteo en el diccionario
            if clave in conteo_claves:
                conteo_claves[clave] += 1
            else:
                conteo_claves[clave] = 1


    conteo_claves_ordenado = {clave: conteo_claves[clave] for clave in sorted(conteo_claves)}
    return conteo_claves_ordenado
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
