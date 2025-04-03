# Ejemplo1 inmutabilidad, funcion pura y sin efectos secundarios
variable_global = 10 #Variable global

def aumentar_variable ():
    return variable_global + 1 # No se modifica la variable global, se retorna un nuevo valor

print(aumentar_variable())

# Ejemplo2 inmutabilidad, funcion pura y sin efectos secundarios
def contar_palabras(texto):
    return len(texto.split())

#Ejemplo3 Uso incorrecto de la funcion pura
contador_global = 0

def contar_palabras_no_funcional(texto):
    global contador_global #Se accede a la variable global
    contador_global = len(texto.split())

#Uso
texto_ejemplo = "Este es un ejemplo sencillo"
contar_palabras_no_funcional(texto_ejemplo)

#Mutable
contar_palabras_no_funcional("Otro texto mas largo")
print(contador_global)