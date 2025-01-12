"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    with open("files/input/data.csv","r") as file:
        lines = file.readlines()
    lista = [(elem.strip().split("\t")[0], elem.strip().split("\t")[3].split(","), elem.strip().split("\t")[4].split(",")) for elem in lines]
    lista

    tuplas = []

    for n in lista:
        resultado = (n[0], len(n[1]), len(n[2]))
        tuplas.append(resultado)
    return tuplas
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
