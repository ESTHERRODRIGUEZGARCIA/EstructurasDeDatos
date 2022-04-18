import ejer1
import ejer2
import ejer3


def elegir():
    variable = input("¿Què ejercicio quiere realizar?: 1, 2 o 3: ")
    if variable == "1":
        ejer1()
    elif variable == "2":
        ejer2()
    elif variable == "3":
        ejer3()
    else:
        print("Seleccione una opción correcta.")
        elegir()
