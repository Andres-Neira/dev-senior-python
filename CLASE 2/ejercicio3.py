'''Ejercicio 2: Conversión de Unidades
Crea un programa que convierta una medida en metros a centímetros
y milímetros. El programa debe pedir al usuario que ingrese una longitud
en metros y luego mostrar el resultado en las dos unidades.'''

mtrs=float(input(" ingrese el numero en metros"))
cmtrs=mtrs*100
mmtrs=mtrs*1000
print(f" la unidad de metros es {mtrs} los centimetros son {cmtrs}, los milimetros son {mmtrs}")