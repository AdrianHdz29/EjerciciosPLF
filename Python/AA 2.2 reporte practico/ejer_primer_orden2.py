def consumo_energia(m, b, c):
    return m * c + b

# Parametros
# Consumo adicional por cada 1% de carga (watts)
m = 2.5
# Consumo base del servidor en reposo (watts)
b = 50

carga = int(input("¿Cual es la carga de trabajo? (Porcentaje)   "))
energia = consumo_energia(m, b, carga)
print(f"Para la carga de {carga}%, el consumo de energia estimado es de {energia} watts.\n")