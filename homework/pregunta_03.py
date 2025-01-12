"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    with open("files/input/data.csv","r") as files:
        lines = files.readlines()
    lista = [elem.strip().split() for elem in lines]

    contador = {}
    for x in lista:
        letra = x[0]
        valor = x[1]

        contador[letra] = contador.get(letra,0) + int(valor)

    resultado = sorted(contador.items())
    return resultado
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
