"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    with open("files/input/data.csv", "r") as files:
        lines = files.readlines()
    lista = [elem.strip().split("\t") for elem in lines]
    letra = [elem[0] for elem in lista]
    letra_uniq = set(letra)

    A = []
    B = []
    C = []
    D = []
    E = []

    for conteo in lista:
        if conteo[0]=="A":
            A.append(int(conteo[1]))
        elif conteo[0]=="B":
            B.append(int(conteo[1]))
        elif conteo[0]=="C":
            C.append(int(conteo[1]))
        elif conteo[0]=="D":
            D.append(int(conteo[1]))
        else:
            E.append(int(conteo[1]))

    conjunto = (A,B,C,D,E)
    #Minimos
    minimos = []
    maximos = []
    for lista1 in conjunto:
        minimos.append(min(lista1))
        maximos.append(max(lista1))

    resultado = []
    letras = ["A", "B", "C", "D", "E"]
    for n in range (0,5):
        resultado.append((letras[n],maximos[n],minimos[n]))
    return resultado
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
