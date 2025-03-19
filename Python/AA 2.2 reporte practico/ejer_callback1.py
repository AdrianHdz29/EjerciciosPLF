import time

# Datos simulados de usuarios en una base de datos
usuarios = [
    {"id": 1, "nombre": "Alice", "edad": 25},
    {"id": 2, "nombre": "Bob", "edad": 30},
    {"id": 3, "nombre": "Charlie", "edad": 35},
    {"id": 4, "nombre": "Diana", "edad": 28}
]

# Función que simula una consulta a la base de datos (con retraso)
def consultar_usuario(id, callback):
    # Simula una consulta a la base de datos y usa un callback para devolver los resultados
    print("Consultando usuario...")
    time.sleep(2)  # Simula un retraso en la consulta
    for usuario in usuarios:
        if usuario["id"] == id:
            # Una vez encontrado el usuario, se llama al callback con el resultado
            callback(usuario)
            return
    # Si no se encuentra el usuario, se llama al callback con un mensaje de error
    callback(None)

# Función de callback para manejar los resultados de la consulta
def procesar_usuario(usuario):
    # Procesa los resultados de la consulta, mostrando la información del usuario o un error
    if usuario:
        print(f"Usuario encontrado: {usuario['nombre']}, Edad: {usuario['edad']}")
    else:
        print("Usuario no encontrado.")

# Ejemplo de uso de la consulta con callback
consultar_usuario(3, procesar_usuario)  # Usuario encontrado
consultar_usuario(5, procesar_usuario)  # Usuario no encontrado
