# Metodo Estatico
# Son funciones que no dependen de la clase
# se identifican son @staticmethod

class Matematica:

    @staticmethod
    def suma(a,b):
        return a+b
   
    @staticmethod
    def resta(a,b):
        return a-b
print(Matematica.suma(10,5))
print(Matematica.resta(20,4))
