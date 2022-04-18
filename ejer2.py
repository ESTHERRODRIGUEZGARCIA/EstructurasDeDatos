# filosofía MVC: Model, View, Controller
# Modelo:
'''
siguiendo la filosofía MVC, escriba un programa que lea dos líneas en la entrada estándar,
las convierta a mayúsculas y las escriba en un archivo. Tenga en cuenta que para beneficiarse
plenamente de las ventajas del design pattern MVC, los atributos, en particular los del modelo, se deben encapsular.
'''
class MVC:
    def __init__(self, modelo, vista, controlador):
        self.linea1 = linea1
        self.linea2 = linea2
        self.modelo = modelo
        self.vista = vista
        self.controlador = controlador
    
    def leer_lineas(self):
        #quiero que el programa em devuekva las lineas en mayusculas
        def mayusculas(self):
            linea1 = "Hola soy Esther"
            linea2 = "Soy una programadora"
            return linea1.upper(), linea2.upper()
        return mayusculas(self)
        
    def ejecutar(self):
        self.controlador.ejecutar()


insertar = MVC(linea1, linea2, controlador)
insertar.ejecutar()

