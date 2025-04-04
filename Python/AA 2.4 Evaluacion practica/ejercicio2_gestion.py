alimentos = [
    "Frijoles Refritos",
    "Coca Cola",
    "Zumo de Naranja",
    "Café de Olla",
    "Gorditas de Chicharrón",
    "Huevos Motuleños"
    ]

ordenado_alimentos = sorted(alimentos)
lista_cadena = ','.join(ordenado_alimentos)
lista_slug = list(map(lambda alim: alim.lower().replace(" ", "-"), ordenado_alimentos))


print("Lista de alimentos de forma Slug:\n", lista_slug)
print("\nLista convertida en cadena:\n", lista_cadena)