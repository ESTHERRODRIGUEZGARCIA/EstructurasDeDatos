# filosofía MVC: Model, View, Controller
# Modelo:
'''
siguiendo la filosofía MVC, escriba un programa que lea dos líneas en la entrada estándar,
las convierta a mayúsculas y las escriba en un archivo. Tenga en cuenta que para beneficiarse
plenamente de las ventajas del design pattern MVC, los atributos, en particular los del modelo, se deben encapsular.
'''
class MVC:
    def __init__(self, modelo, vista, controlador):
        self.modelo = modelo
        self.vista = vista
        self.controlador = controlador
    def ejecutar(self):
        self.controlador.ejecutar()

linea1 = "Hola soy Esther"
linea2 = "Soy una programadora"
insertar = MVC(linea1, linea2, controlador)
