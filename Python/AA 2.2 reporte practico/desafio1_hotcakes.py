def preparar_hotcakes():
    return "🥞"

def ordenar_hotcakes(num_piezas):
    piezas_hotcakes = [preparar_hotcakes() for _ in range(num_piezas)]
    return piezas_hotcakes

hotcakes_familia = ordenar_hotcakes(int(input('Ingresar el numero integrantes de su familia:  ')))
print(hotcakes_familia)