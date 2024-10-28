'''Ejercicio: Calculadora Avanzada 📐
Crea una calculadora que tome dos números y un operador del usuario (+, -, *, /, %, **).
El programa debe realizar la operación correspondiente y mostrar el resultado.
Si el operador ingresado no es válido, el programa debe mostrar un mensaje de error.

Instrucciones:
Solicita al usuario que ingrese dos números.
Solicita al usuario que ingrese un operador.
Usa operadores aritméticos para realizar la operación correspondiente.
Utiliza operadores lógicos para validar el operador ingresado.'''

num1=float(input("Digite el numero 1"))
num2=float(input("Digite el numero 2"))
opr=input("escriba la operación a realizar sum(suma),res(resta),mult(multiplicación),div(división),mod(residuo de división), pot(potencia)")
sum=num1+num2
res=num1-num2
mult=num1*num2
div=num1/num2
mod=num1%num2
pot=num1**num2
if(opr=="sum"):
    print(f" la suma es {sum}")
elif(opr=="res"):
    print(f"la resta es {res}")
elif(opr=="mult"):
    print(f"la multiplicación es{mult}")
elif(opr=="div"):
    print(f"la división es{div}")
elif(opr=="mod"):
    print(f"El residuo es es{mod}")
elif(opr=="pot"):
    print(f"la Potencia es{pot}")
else:
    print(f"error")