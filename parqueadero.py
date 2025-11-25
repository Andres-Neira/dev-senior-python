import tkinter as tk
from tkinter import ttk,messagebox
import datetime

class vehiculo:
    def __init__(self,placa,hora_entrada):
        self.placa=placa
        self.hora_entrada=hora_entrada
    
    def calcularTiempo(self):
        hora_salida=datetime.datetime.now()
        tiempo_total=hora_salida-self.hora_entrada
        return tiempo_total.total_seconds()/60

class ParqueaderoApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Control del parqueadero")
        self.root.geometry("500x400")
        self.vehiculos={}

        # Entrada de la plana
        tk.Label(root,text="Placa de veiculo ").pack(pady=5)# texto
        self.entry_placa=tk.Entry(root)# caja de texto
        self.entry_placa.pack(pady=5)

        # botones
        tk.Button(root,text="Registro Entrada", command=self.registro_entrada).pack(pady=5)
        tk.Button(root,text="Registro Salida", command=self.registrar_salida).pack(pady=5)

        #tabla de vehiculos
        self.tree = ttk.Treeview(root,columns=("Placa","Hora de entrada"), show="headings")
        self.tree.heading("Placa",text="Placa")
        self.tree.heading("Hora de entrada",text="Hora de entrada")
        self.tree.pack(pady=10,fill="both",expand=True)

    def registro_entrada(self):
        placa=self.entry_placa.get().upper()
        print(placa)
        if placa in placa not in self.vehiculos:
            hora_actual=datetime.datetime.now().strftime("%H:%M:%S")
            print(hora_actual)
            self.vehiculos[placa] = vehiculo(placa,datetime.datetime.now())

            self.tree.insert("","end",iid=placa, values=(placa,hora_actual))

    def registrar_salida(self):
        placa=self.entry_placa.get().upper()
        print(placa)
        if placa in self.vehiculos:
            vehiculo =self.vehiculos.pop(placa)
            tiempo_parque=vehiculo.calcularTiempo()
            print("Tiempo de parque")

                # Eliminar de la tabla
            self.tree.delete(placa)
            messagebox.showinfo(f"Salida" ,F"Placa : {placa}      Tiempo : {tiempo_parque}")
        else:
            messagebox.showerror("Error "," vehiculo no encontrado")



ventana=tk.Tk()
aplicacion =ParqueaderoApp(ventana)
ventana.mainloop()

