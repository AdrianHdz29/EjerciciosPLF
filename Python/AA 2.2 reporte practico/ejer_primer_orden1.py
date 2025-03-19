# Primer orden
# Latencia de una red en funcion del tamaño de los paquetes
# Modelo lineal

def latencia(m, c, p):
    return m * p + c

# 50 microsegundos por byte
m = 0.00005
# 20 milisegundos de latencia fija
c = 0.02

paquete = int(input("¿Cuál es el tamaño del paquete a estimar?"))
tiempo_e = latencia(m, c, paquete)
print(f"Timepo estimado del paquete de {paquete} bytes:  {tiempo_e:.4f} segundos")
