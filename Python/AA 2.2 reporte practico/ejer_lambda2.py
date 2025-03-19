# Función lambda para calcular el número de redes disponibles según la máscara de subred (en notación CIDR)
calcular_redes_disponibles = lambda mascara_subred: 2 ** (32 - mascara_subred)

# Ejemplo de direcciones IP con diferentes máscaras
mascaras = [24, 25, 26, 28, 30]

# Imprimir el número de redes disponibles para cada máscara
print("Cálculo de redes disponibles en IPv4:")
for mascara in mascaras:
    redes = calcular_redes_disponibles(mascara)
    print(f"Máscara /{mascara} => Redes Disponibles: {redes}")
