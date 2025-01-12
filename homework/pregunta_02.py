"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    with open("files/input/data.csv","r") as files:
        lines = files.readlines()

    lista = [elem.strip().split("\t") for elem in lines]
    letra = [valor[0] for valor in lista]

    valores_unicos = set (letra)
    #valores_unicos

    A = 0
    B = 0
    C = 0
    D = 0
    E = 0

    for l in letra:
        if l=="A":
            A +=1
        elif l=="B":
            B +=1
        elif l=="C":
            C +=1
        elif l=="D":
            D +=1
        else:
            E +=1

    tuplas = [("A",A),("B",B),("C",C),("D",D),("E",E)]
    return tuplas


    #Otra forma:
    # with open("files/input/data.csv","r") as files:
    #     lines = files.readlines()
    # Contar letras en la primera columna
    # contador = {}
    # for line in lines:
    #     letra = line.split("\t")[0]  # Extraer la letra de la primera columna
    #     contador[letra] = contador.get(letra, 0) + 1

    # # Convertir a lista de tuplas y ordenar
    # resultado = sorted(contador.items())
    # print(resultado)

    # contador.get(letra, 0):

    # Busca la clave letra en el diccionario.
    # Si la clave existe, devuelve su valor (el conteo actual de esa letra).
    # Si la clave no existe, devuelve el valor por defecto 0.
    # + 1:

    # Incrementa el conteo de la letra en uno.
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
