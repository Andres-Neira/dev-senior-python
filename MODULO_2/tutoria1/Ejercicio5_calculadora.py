'''5. Clase `Calculadora`: Diseña una clase `Calculadora`
con un método estático `suma` que reciba dos números y devuelva la suma de ellos.
Ejemplo:
print(Calculadora.suma(3, 4))  # Salida: 7'''

class Calculadora:

    @staticmethod
    def suma(num1,num2):
        return num1+num2

print(Calculadora.suma(5,56))