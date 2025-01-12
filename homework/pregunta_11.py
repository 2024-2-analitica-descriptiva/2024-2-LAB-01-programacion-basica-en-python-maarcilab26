"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    with open("files/input/data.csv","r") as file:
        lines = file.readlines()
    lista = [(elem.strip().split("\t")[3].split(","), elem.strip().split("\t")[1]) for elem in lines]
    lista

    diccionario = {}

    for sublista, valor in lista:
        valor = int(valor)
        for letra in sublista:
            if letra in diccionario:
                diccionario[letra]+= valor
            else:
                diccionario[letra] = valor

    diccionario_ordenado = {letra: diccionario[letra] for letra in sorted(diccionario)}
    return diccionario_ordenado

    #NOTA: si aplico solo sorted(diccionario) devuelve una lista de las claves del diccionario ordenadas alfabéticamente.

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
