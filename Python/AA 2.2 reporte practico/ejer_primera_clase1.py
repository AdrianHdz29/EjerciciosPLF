# Función que filtra logs según una condición dada
def filtrar_logs(logs, criterio):
    return [log for log in logs if criterio(log)]

# Funciones de primera clase
# Función de criterio 1: Filtra solo errores
def es_error(log):
    return "ERROR" in log
# Función de criterio 2: Filtra solo accesos exitosos
def es_acceso_exitoso(log):
    return "200 OK" in log
# Función de criterio 3: Filtra solo advertencias
def es_advertencia(log):
    return "WARNING" in log

# Simulación de logs de un servidor
logs_servidor = [
    "[INFO] Servidor iniciado",
    "[ERROR] Conexión fallida a la base de datos",
    "[WARNING] Uso alto de CPU",
    "[INFO] Usuario autenticado correctamente",
    "[ERROR] Intento de acceso no autorizado",
    "[INFO] Petición HTTP 200 OK recibida"
]

# Aplicamos diferentes filtros usando funciones como parámetros
logs_errores = filtrar_logs(logs_servidor, es_error)
logs_exitosos = filtrar_logs(logs_servidor, es_acceso_exitoso)
logs_advertencias = filtrar_logs(logs_servidor, es_advertencia)

# Mostramos los resultados
print("📌 Logs de errores:")
for log in logs_errores:
    print(log)

print("\n📌 Logs de accesos exitosos:")
for log in logs_exitosos:
    print(log)

print("\n📌 Logs de advertencias:")
for log in logs_advertencias:
    print(log)