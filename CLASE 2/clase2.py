var1=100
var2=100
var=var1+var2
print(f"el valor var: {var} es la suma de var1 y var 2")


ancho=1203
alto=876
area=ancho*alto
print(f"Siendo el ancho {ancho} y el alto {alto} , el area es {area}")

# variable de tipo int
a= 30
b= 30
# variable tipo int
d=30.0

c=a**b
print(c)

# variable tipo str
f="30.0"
g="3.0"

# variable tipo bool apartir de operación racional
x = a == b 
print(x)

# operadorres logicos, and or,not
# y = True  and  False (&& || !)
y = x and a == c
z = not y
# not niega o combierte contrario el booleano

#Operadores logicos y relacionales
y = (a == b and d < a) or (f == g) 

z = a*b == b*d and a*d < b*a

print(f"Resultado directo de operacion relacional y logica:{(a == b and d < a)}")

# variable tipo str
peso = "80"

# Conversion de str a int
# str = "80"
pesoNumEnt = int(peso)
print(peso)

# Conversion de str a float
# str = "80.0"
pesoNumFloat = float(peso) + 0.1
# str = "80.1"

# str value of 80
peso2 = str(pesoNumFloat)

# "80" == "80.0"
# print(peso == peso2)

# 80 == 80.0
# print(pesoNumEnt == pesoNumFloat)

xy = (a == b and d < a)
y = xy or (f == g) 