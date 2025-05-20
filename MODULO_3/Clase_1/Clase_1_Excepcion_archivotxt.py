def abrir_archivo():
    try:
        with open('datos.txt','r') as archivo:
            contenido = archivo.read()
            numero = int(contenido.strip())
            print(numero)
    except Exception as e:
        print('Se produjo un error')

abrir_archivo()