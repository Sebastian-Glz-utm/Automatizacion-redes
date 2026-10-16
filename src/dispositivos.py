dispositivos = [
    {
    "nombre": "R1",
    "tipo": "Router",
    "ip": "10.1.1.1",
    "estado": "Activo",
    "fabricante": "Cisco",
    "protocolo": "OSPF"
    },
    {
    "nombre": "R2",
    "tipo": "Router",
    "ip": "192.168.8.243",
    "estado": "Activo",
    "fabricante": "Cisco",
    "protocolo": "OSPF"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "estado": "Activo"
    }
]
def mostrar_dispositivo(dispositivo):
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
for dispositivo in dispositivos:
    mostrar_dispositivo(dispositivo)
    print("--------------------")
