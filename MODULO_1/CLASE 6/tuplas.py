paises=('colombia','mexico','ecuador','venezuela')
print(type(paises))
print(len(paises))
print(paises[2])

for pais in paises:
    print(pais)

paisesLista= list(paises)
paisesLista[1]='argentina'
paises=tuple(paisesLista)
print(paises)