# Datos simulados de servidores (nombre, estado, carga CPU (%), espacio libre en disco (%))
servidores = [
    {"nombre": "Servidor_A", "estado": "activo", "cpu": 30, "espacio": 60},
    {"nombre": "Servidor_B", "estado": "inactivo", "cpu": 0, "espacio": 80},
    {"nombre": "Servidor_C", "estado": "activo", "cpu": 90, "espacio": 20},
    {"nombre": "Servidor_D", "estado": "activo", "cpu": 50, "espacio": 10},
]

# Diferentes criterios de monitoreo
# Devuelve True si el servidor está activo
def esta_disponible(servidor):
    return servidor["estado"] == "activo"

# Devuelve True si el servidor tiene más del 80% de carga de CPU
def esta_sobrecargado(servidor):
    return servidor["cpu"] > 80

# Devuelve True si el servidor tiene menos del 15% de espacio libre en disco
def tiene_poco_espacio(servidor):
    return servidor["espacio"] < 15

# FUNCIÓN DE ORDEN SUPERIOR
# Filtra servidores según el criterio dado (una función como argumento)
def filtrar_servidores(servidores, criterio):
    return [servidor for servidor in servidores if criterio(servidor)]

# Uso de la función de orden superior
servidores_activos = filtrar_servidores(servidores, esta_disponible)
servidores_sobrecargados = filtrar_servidores(servidores, esta_sobrecargado)
servidores_con_poco_espacio = filtrar_servidores(servidores, tiene_poco_espacio)

print("\nServidores activos:", [s["nombre"] for s in servidores_activos])
print("\nServidores sobrecargados:", [s["nombre"] for s in servidores_sobrecargados])
print("\nServidores con poco espacio:", [s["nombre"] for s in servidores_con_poco_espacio])
