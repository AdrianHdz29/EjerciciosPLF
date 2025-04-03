def agregar_asignatura(lista):
    asig_nueva = input("Otorgue una asignatura(ponga 'no' para salir):   ")
    if asig_nueva == "no":
        return lista
    return agregar_asignatura(lista + [asig_nueva])

asignaturas = ["Graficación", "Automatas", "Investigacion"]

nueva_lista = agregar_asignatura(asignaturas)
print(nueva_lista)