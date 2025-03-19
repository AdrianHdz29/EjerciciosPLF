from datetime import datetime

# Datos simulados de tareas de un proyecto
tareas = [
    {"nombre": "Desarrollar módulo de autenticación", "estado": "completado", "fecha_entrega": "2025-03-15", "prioridad": 3},
    {"nombre": "Realizar pruebas de integración", "estado": "pendiente", "fecha_entrega": "2025-03-20", "prioridad": 2},
    {"nombre": "Documentar la API", "estado": "completado", "fecha_entrega": "2025-03-10", "prioridad": 1},
    {"nombre": "Implementar control de acceso", "estado": "pendiente", "fecha_entrega": "2025-03-05", "prioridad": 3},
    {"nombre": "Desarrollar interfaz de usuario", "estado": "pendiente", "fecha_entrega": "2025-03-25", "prioridad": 2},
]

# Diferentes criterios de análisis
# Devuelve True si la tarea está completada
def esta_completada(tarea):
    return tarea["estado"] == "completado"

# Devuelve True si la tarea está retrasada
def esta_retrasada(tarea):
    fecha_actual = datetime.now()
    fecha_entrega = datetime.strptime(tarea["fecha_entrega"], "%Y-%m-%d")
    return tarea["estado"] == "pendiente" and fecha_entrega < fecha_actual

# Devuelve True si la tarea tiene prioridad alta
def es_critica(tarea):
    return tarea["prioridad"] == 3

# FUNCIÓN DE ORDEN SUPERIOR
# Filtra las tareas según el criterio dado (una función como argumento)
def filtrar_tareas(tareas, criterio):
    return [tarea for tarea in tareas if criterio(tarea)]

# Uso de la función de orden superior
tareas_completadas = filtrar_tareas(tareas, esta_completada)
tareas_retrasadas = filtrar_tareas(tareas, esta_retrasada)
tareas_criticas = filtrar_tareas(tareas, es_critica)

print("Tareas completadas:", [t["nombre"] for t in tareas_completadas])
print("Tareas retrasadas:", [t["nombre"] for t in tareas_retrasadas])
print("Tareas críticas:", [t["nombre"] for t in tareas_criticas])
