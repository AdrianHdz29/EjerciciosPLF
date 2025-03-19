import time

# Simulación de contenido de archivo
contenido_archivo = """
Ingeniería en Sistemas Computacionales es una carrera que se enfoca en el diseño, desarrollo y mantenimiento de software y sistemas computacionales. 
Los ingenieros en sistemas están capacitados para abordar problemas complejos en diversas áreas como la programación, redes, bases de datos, y mucho más.
La carrera es fundamental para el avance tecnológico y la innovación en diversas industrias.
"""

# Función que simula la lectura de un archivo de texto
def leer_archivo(callback):
    # Simula la lectura de un archivo de texto con un retraso y luego ejecuta el callback con el contenido
    print("Leyendo el archivo...")
    time.sleep(2)  # Simula un retraso en la lectura del archivo
    callback(contenido_archivo)

# Función de callback para procesar el contenido del archivo
def procesar_contenido(contenido):
    # Procesa el contenido del archivo: en este caso, contar el número de palabras
    palabras = contenido.split()  # Se divide el contenido en palabras
    num_palabras = len(palabras)
    print(f"El archivo tiene {num_palabras} palabras.")
    
    # También se pueden realizar otros análisis, como buscar palabras clave
    palabras_clave = ["ingeniería", "sistemas", "tecnológico"]
    for palabra in palabras_clave:
        if palabra in contenido:
            print(f"Se encontró la palabra clave '{palabra}' en el archivo.")
        else:
            print(f"No se encontró la palabra clave '{palabra}' en el archivo.")

# Uso de la función con callback
leer_archivo(procesar_contenido)
