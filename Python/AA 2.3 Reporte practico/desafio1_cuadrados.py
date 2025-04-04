'''
A partir del código base modifica la función cuadradosLista utilizando cualquier combinación de map(), filter(), ó reduce().  
La función debería devolver un nuevo arreglo que contenga los cuadrados únicamente de los enteros positivos (los números decimales no son enteros) cuando se le pase un arreglo de números reales.  
Un ejemplo de un arreglo de números reales es [-3, 4.8, 5, 3, -3.2].  

Nota: La función no debe usar ningún tipo de bucles for o while ni la función forEach().
'''

def cuadradosLista(arreglo):

    # Escribir código aquí
    solo_enteros = list(filter(lambda numero: isinstance(numero, int) and numero >= 0, arreglo))
    cuadrados = list(map(lambda x: x**2, solo_enteros))

    return cuadrados # Devolver una lista con los cuadrados de los enteros positivos

# Ejemplo de uso
cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)
