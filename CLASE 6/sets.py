# no se pueden modificar elementos 
# no se pueden repetir

lenguajes={'java','python','javascrib'}
print(lenguajes)
print(len(lenguajes))
print('java' in lenguajes)
lenguajes.add('go')
print(lenguajes)
for lenguaje in lenguajes:
    print(lenguaje)
lenguajes.remove('java')
print(lenguajes)
lenguajes.discard('python')
print(lenguajes)