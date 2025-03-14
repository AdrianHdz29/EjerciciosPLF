def preparar_pizza():
    return "🍕"
def preparar_hamburguesa():
    return "🍔"
def preparar_hotdog():
    return "🌭"

def ordenar_alimento(preparar, num_porcion):
    porciones_alimentos = [preparar for _ in range(num_porcion)]
    bonus = calcular_bonus(num_porcion)
    return porciones_alimentos, bonus

def calcular_bonus(num_porcion):
    if num_porcion > 2 :
        return "🥤 Coca gratis"
    else:
        return ""



alimento_grupo_a = ordenar_alimento(preparar_hamburguesa(), int(input('Ingresa la porcion de la orden:   ')))
alimento_grupo_b = ordenar_alimento(preparar_hotdog(), int(input('Ingresa la porcion de la orden:   ')))
alimento_grupo_c = ordenar_alimento(preparar_pizza(), int(input('Ingresa la porcion de la orden:   ')))

print(
    alimento_grupo_a,    
    alimento_grupo_b,
    alimento_grupo_c
)