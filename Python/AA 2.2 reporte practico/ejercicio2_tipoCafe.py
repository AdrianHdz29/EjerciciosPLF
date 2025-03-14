def preparar_cafe_ame():
    return "Cafe americano"
def preparar_cafe_olla():
    return "Cafe de olla"

def ordenar_cafe(preparar, num_tazas):
    tazas_cafe = [preparar for _ in range(num_tazas)]
    return tazas_cafe


cafe_grupo_a = ordenar_cafe(preparar_cafe_ame(), 10)
cafe_grupo_b = ordenar_cafe(preparar_cafe_olla(), 12)

print(cafe_grupo_a, cafe_grupo_b)