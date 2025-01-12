"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
#PREGUNTA1
#Nota: cuando se pega la ruta completa, se pone la r adelante si no se desea cambiar el \, sino, se deben cambiar todos por / o \\
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    lista = [z.strip().split("\t") for z in lines]
    col2 = sum([int(elem[1]) for elem in lista])
    
    return col2

    #Así se verifica que los datos están como string y que se deben convertir a entero
    # for item in col2:
    #     print(item, type(item))

    #Otra forma de abrir el archivo:
    # file = open(r"C:\Users\Maria Camila Arcila\Documents\GitHub\AnaliticaDescriptiva\Labs\Ensayo\files\input\data.csv", "r").readlines()

    #Otra forma de hacer la suma
    # suma = 0
    # for z in lista:
    #     suma += int(z[1])
    # suma

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """