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
    def __init__(self, naturaleza, iva):
        self.naturaleza = naturaleza
        self.ALIMENTARIA = 0.055
        self.SERVICIO = 0.2
        self.iva = iva

    def __str__(self):
        return self.naturaleza

class Producto(Naturaleza):
    def facturar(self):
        if self.naturaleza == Naturaleza.ALIMENTARIA:
            return self.precio_neto * 1.055
        elif self.naturaleza == Naturaleza.SERVICIO:
            return self.precio_neto * 1.2
        else:
            return self.precio_neto

class FactoryFactura:
    def __init__(self, producto):
        self.producto = producto

    def facturar(self):
        return producto(self.iva)


Naturaleza = Naturaleza()

producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5%
precio_neto = FactoryFactura.crear(producto).facturar()
print(precio_neto)
# 105.5

producto = Producto(Naturaleza.SERVICIO) # IVA 20%
precio_neto = FactoryFactura.crear(producto).facturar()
print(precio_neto)
# 120

