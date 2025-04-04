from functools import reduce

lista_ventas = [1500, 2500, 3200, 4500, 6000, 1200, 8000]
cambio_dolar = 20.46

promedio_ventas = round(reduce(lambda aux, venta: aux + venta, lista_ventas, 0) / len(lista_ventas), 2)
ventas_dolares = list(map(lambda venta: round(venta/cambio_dolar, 2), lista_ventas))
ventas_mayores = list(filter(lambda venta: venta > 150, ventas_dolares))
suma_ventas = round(reduce(lambda aux, venta: aux + venta, ventas_mayores, 0), 2)

print("\nPromedio de las ventas en pesos:   ", promedio_ventas)
print("Ventas en dolares:   ", ventas_dolares)
print("Ventas en dolares mayores a 150:   ", ventas_mayores)
print("Suma de las ventas mayores:    ", suma_ventas)