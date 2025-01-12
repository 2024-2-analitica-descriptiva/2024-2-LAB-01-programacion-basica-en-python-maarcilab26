"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    with open("files/input/data.csv", "r") as files:
        lines = files.readlines()
    lista = [(int(elem.strip().split("\t")[1]), elem.strip().split("\t")[0]) for elem in lines]
    lista

    #NOTA: no se puede usar la función dict, porque en ese caso, si las claves se repiten, conserva únicamente el último valor

    #Crear un diccionario para acumular los valores por clave
    diccionario = {}

    for clave, valor in lista:
        diccionario[clave] = diccionario.get(clave, [])
        diccionario[clave].append(valor)


    resultado = sorted(diccionario.items())
    return resultado
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
