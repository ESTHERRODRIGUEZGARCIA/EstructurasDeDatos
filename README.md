# EstructurasDeDatos
Ejercicios de Estructuras de Datos

# EJERCICIO 1

````
class Bloque:
    # Un bloque es un conjunto de instrucciones ejecutadas 
    # unas detrás de otras. 
    def __init__(self): 
        # Por defecto, un bloque no contiene ninguna instrucción. 
        self.instrucciones = [] 
 
    def agregarInstruction(self, instruccion): 
        self.instrucciones.append(instruccion) 
 
class Si: 
    # Representa una instrucción 'if'. 'condicion' es una cadena 
    # de caracteres que contiene la evaluación de la condición, 
    # 'entonces' es el bloque de instrucciones ejecutadas si la condición 
    # se verifica, 'si_no' es el bloque de instrucciones ejecutadas 
    # si no se verifica. 
 
    def __init__(self, condicion, entonces, si_no): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.si_no = si_no 
 
class MientrasQue: 
    # Representa una instrucción 'while'. 
    # 'condicion' es una cadena que contiene el valor evaluado 
    # para decidir si el bucle continúa o no, 
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle. 
    def __init__(self, condicion, bloque): 
        self.condicion = condicion
        self.bloque = bloque

class Mostrar:
# Una instrucción para mostrar un mensaje
    # en salida estándar.
    def __init__(self, mensaje):
        self.mensaje = mensaje


mostrar_ok = Mostrar('"OK"')
mostrar_ko = Mostrar('"KO"')
alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko)
bloque_alternativa = Bloque()
bloque_alternativa.agregarInstruction(alternativa)
bucle = MientrasQue(True, bloque_alternativa)

````
# EJERCICIO 2

````

# filosofía MVC: Model, View, Controller
# Modelo:
'''
siguiendo la filosofía MVC, escriba un programa que lea dos líneas en la entrada estándar,
las convierta a mayúsculas y las escriba en un archivo. Tenga en cuenta que para beneficiarse
plenamente de las ventajas del design pattern MVC, los atributos, en particular los del modelo, se deben encapsular.
'''
import sys
import os
linea1 = "Hola soy Esther"
linea2 = "Soy una programadora"
class MVC:
    def __init__(self, linea1, linea2):
        self.linea1 = linea1
        self.linea2 = linea2
    
    def ejecutar(self):
        self.controlador.ejecutar()

    def leer_lineas(self):
        #quiero que el programa em devuekva las lineas en mayusculas
        def mayusculas(self):
            insertar = open("ejercicio2.txt", "w")
            insertar.write(linea1.upper)
            insertar.write(linea2.upper)
            insertar.close()
            print("Se ha creado el archivo ejercicio2.txt")
            os.remove("ejercicio2.txt")
        return mayusculas(self)



````

