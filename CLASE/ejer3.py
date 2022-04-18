# Enunciado: Implementar un programa que factura productos por valor de 100, con la tasa de IVA correcta, según sean productos de alimentación o servicios.
''''
comportamiento:
producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 105.5 
 
producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 120 '''

class Naturaleza:
    def __init__(self, naturaleza, ALIMENTARIA, SERVICIO):
        self.naturaleza = naturaleza
        self.ALIMENTARIA = 0.055
        self.SERVICIO = 0.2
    
    def alimentaria(self):
        return self.ALIMENTARIA
    
    def servicio(self):
        return self.SERVICIO

    def naturaleza(self):
        return self.naturaleza

    def precio_neto(self):
        return self.precio_neto

class Producto(Naturaleza):
    def comprafinal(self):
        precio_inicial = 100
        compra = int(input("¿Qué producto quiere comprar?: Alimentación(1) o Servicio(2): "))
        if compra == 1:
            precio_neto = precio_inicial * self.alimentaria()
            return precio_neto
        elif compra == 2:
            precio_neto = precio_inicial * self.servicio()
            return precio_neto
        else:
            print("Seleccione una opción correcta. ")

    comprafinal()
Producto()