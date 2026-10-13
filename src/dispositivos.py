dispositivos = [
    {
       "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "loopback": "1.1.1.1",
        "interfaz": "GigabitEthernet0/0",
        "estado": "Activo"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "loopback": "2.2.2.2",
        "interfaz": "GigabitEthernet0/0",
        "estado": "Activo"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "estado": "Activo"
    }
]

print("")
for dispositivo in dispositivos:
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
    print("--------------------")