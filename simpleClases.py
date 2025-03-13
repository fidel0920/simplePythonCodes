class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_detalles(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}'

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas

    def tocar_bocina(self):
        return '¡aaaaaaaaaaauuuuuua!'

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo 

    def hacer_caballito(self):
        return '¡se trono la transmision jaja!'

class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.capacidad_carga = capacidad_carga  

    def descargar(self):
        return 'ostia tio, que me he quedado sin abs'

coche = Coche('Toyota', 'Corolla', 2020, 4)
moto = Motocicleta('Honda', 'CBR', 2019, 'Deportiva')
camion = Camion('Mercedes', 'Actros', 2018, 10)

print(coche.mostrar_detalles())
print(coche.tocar_bocina())

print(moto.mostrar_detalles())
print(moto.hacer_caballito())

print(camion.mostrar_detalles())
print(camion.descargar())
