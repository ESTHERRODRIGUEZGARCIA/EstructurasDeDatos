import CLASE.ejer1 as ejer1
import CLASE.ejer2 as ejer2
import CLASE.ejer3 as ejer3


def elegir():
    variable = input("¿Què ejercicio quiere realizar?: 1, 2 o 3: ")
    if variable == "1":
        print("Ejercicio 1: \n")
        ejer1()
    elif variable == "2":
        print("Ejercicio 2: \n")
        ejer2()
    elif variable == "3":
        print("Ejercicio 3: \n")
        ejer3()
    else:
        print("Seleccione una opción correcta. ")
        elegir()

if __name__ == "__main__":
    elegir()
    
