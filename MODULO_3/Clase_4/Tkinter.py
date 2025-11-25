import tkinter as tk

def convertir():
    try:
        celsius=float(entry.get())
        fahreinheit=(celsius*(9/5))+32
        resultado.config(text=f"resultado = {fahreinheit} °f")
    except:
        resultado.config(text="Ingrese un número valido")


# configuración de la ventana
root = tk.Tk()
root.title("Conversor de temperatura")
root.geometry("300x200")

# widgets : se utilizan dentro de la aplicación son aplicaciones para el front

# Widgets
#.label permite agregar las configuraciones para que funcione , se le añade pady para que se vea, EL PADY NO LO MUESTRA LO MUESTRA ES EL PACK
tk.Label(root, text="Ingrese temperatura en °C").pack(pady=5)
# se crea la variable entry para que funcione entry
entry=tk.Entry(root)
# se añade este espacio para añadir la opción de ingresar el que muestra esto lo hace pady
entry.pack(pady=5)

# Se añade el resultado con la variable
resultado = tk.Label(root,text="El resultado es : ")
resultado.pack(pady=5)


# se añade un boton para ingresar información
tk.Button(root,text="CONVERTIR ", command=convertir).pack(pady=5)
root.mainloop()