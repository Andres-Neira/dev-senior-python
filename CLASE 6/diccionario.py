conceptoProgramacion={'IDE':'Entorno de desarrollo','OPP':'Programación orientada a objetos'}
print(conceptoProgramacion)
print(len(conceptoProgramacion))
print(conceptoProgramacion['IDE'])
print(conceptoProgramacion.get('OPP'))

conceptoProgramacion['DBMS']='Database Managment Sistem'
for keys,value in conceptoProgramacion.items():
    print(keys, value)
