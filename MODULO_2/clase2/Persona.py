class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self._edad=edad
        self.__cuentabancaria=123456

    def mostrarInformacion(self):
        return f'Nombre : {self.nombre} edad : {self._edad}'
    def __mostrarCuenta(self):
        return f'Cuenta Bancaria : {self.__cuentabancaria}'
    def mostrarInformacionCompleta(self):
        return self.__mostrarCuenta

persona1= Persona('Andres Neira',25)
print(persona1.nombre)
print(persona1._edad)
print(persona1.mostrarInformacion())
print(persona1.mostrarInformacionCompleta())
# public
# protegido = _variable
# privaado = __variable
