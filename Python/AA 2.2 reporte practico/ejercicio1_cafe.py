def preparar_cafe():
    return "Café"

def ordenar_cafe(numero_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_para_grupo = ordenar_cafe(int(input('Ingresa tu orden')))
print(cafe_para_grupo)