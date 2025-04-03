# a = ["bbdd"]
# b = a + ["web"]

# print(a)
# print(b)

asignaturas_viii = ["Inteligencia Artificial"]
mas_asignaturas = asignaturas_viii + ["Programacion de Backend"]

print(asignaturas_viii)
print(mas_asignaturas)

def agregar_asignatura(lista, asignatura):
    return lista + [asignatura]

print(agregar_asignatura(asignaturas_viii, input("Otorgue una asignatura para añadir a la lista:  ")))