"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():

    with open("files/input/data.csv", "r") as files:
        lines = files.readlines()
    lista = [elem.strip().split("\t")[4].split(",") for elem in lines]

    # Crear un diccionario para acumular los valores por clave
    valores_por_clave = {}

    for sublista in lista:
        for par in sublista:
            clave, valor = par.split(":")
            valor = int(valor)
            if clave not in valores_por_clave:
                valores_por_clave[clave] = []
            valores_por_clave[clave].append(valor)

    # Calcular mínimo y máximo por clave
    resultado = []
    tuplas = valores_por_clave.items()
    for clave, valores in tuplas:
        minimo = min(valores)
        maximo = max(valores)
        resultado.append((clave, minimo, maximo))

    # Ordenar el resultado por clave alfabéticamente
    resultado.sort()

    return resultado
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
