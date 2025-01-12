"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    with open("files/input/data.csv","r") as file:
        lines = file.readlines()
    lista = [(elem.strip().split("\t")[0], elem.strip().split("\t")[4].split(",")) for elem in lines]

    diccionario = {}

    for letra, sublista in lista:
        for pares in sublista:
            clave, valor = pares.split(":")
            if letra in diccionario:
                diccionario[letra] += int(valor)
            else:
                diccionario[letra] = int(valor)

    diccionario_ordenado = {letra: diccionario[letra]  for letra in sorted(diccionario)}
    return diccionario_ordenado
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
