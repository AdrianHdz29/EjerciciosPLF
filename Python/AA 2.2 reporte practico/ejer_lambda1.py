# Lista de estudiantes con su nombre y calificación
estudiantes = [
    {"nombre": "Alice", "calificacion": 75},
    {"nombre": "Bob", "calificacion": 85},
    {"nombre": "Charlie", "calificacion": 90},
    {"nombre": "Diana", "calificacion": 65},
    {"nombre": "Eva", "calificacion": 95}
]

# 1. Filtrar estudiantes con calificación mayor a 80 utilizando lambda
estudiantes_filtrados = list(filter(lambda estudiante: estudiante["calificacion"] > 80, estudiantes))

# Mostrar los estudiantes filtrados
print("Estudiantes con calificación mayor a 80:")
for estudiante in estudiantes_filtrados:
    print(f"{estudiante['nombre']} - {estudiante['calificacion']}")

# 2. Ordenar estudiantes por nombre en orden alfabético utilizando lambda
estudiantes_ordenados = sorted(estudiantes, key=lambda estudiante: estudiante["nombre"])

# Mostrar estudiantes ordenados
print("\nEstudiantes ordenados por nombre:")
for estudiante in estudiantes_ordenados:
    print(f"{estudiante['nombre']} - {estudiante['calificacion']}")
