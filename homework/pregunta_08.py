"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    with open("files/input/data.csv", "r") as files:
        lines = files.readlines()
    lista = [(int(elem.strip().split("\t")[1]), elem.strip().split("\t")[0]) for elem in lines]
    lista

    #NOTA: no se puede usar la función dict, porque en ese caso, si las claves se repiten, conserva únicamente el último valor

    #Crear un diccionario para acumular los valores por clave
    diccionario = {}

    for clave, valor in lista:
        diccionario[clave] = diccionario.get(clave, [])
        if valor not in diccionario.get(clave,[]):
            diccionario[clave].append(valor)

    for clave in diccionario:
        diccionario[clave] = sorted(diccionario[clave])

    resultado = sorted(diccionario.items())
    return resultado
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
