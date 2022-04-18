from CLASE import *


def elegir():
    variable = input("¿Què ejercicio quiere realizar?: 1, 2 o 3: ")
    if variable == "1":
        print("Ejercicio 1: \n")
        from CLASE import ejer1
    elif variable == "2":
        print("Ejercicio 2: \n")
        from CLASE import ejer2

    elif variable == "3":
        print("Ejercicio 3: \n")
        from CLASE import ejer3
    else:
        print("Seleccione una opción correcta. ")

elegir()

if __name__ == "__main__":
    elegir()

