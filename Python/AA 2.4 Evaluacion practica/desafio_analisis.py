import tkinter as tk  # Importa la librería Tkinter para la construcción de GUI
from functools import reduce  # Se importa reduce
from tkinter import messagebox as mb  # Permite desplegar ventanas de mensaje

### Datos
# Lista de asignaturas
asignaturas = [
    {
        "asignatura":"Inteligencia Artificial",
        "puntos":0
    },
    {
        "asignatura":"Administración de Redes",
        "puntos":0
    },
    {
        "asignatura":"Programación de Móviles",
        "puntos":0
    }
]

# Lista de aspectos a evaluar
aspectos = [
    {
        "pregunta": "¿Cómo calificaría el contenido de la asignatura?",
        1: "1 - Mal explicado",
        2: "2 - Deficiente",
        3: "3 - Aceptable",
        4: "4 - Claro",
        5: "5 - Bien explicado"
    },
    {
        "pregunta": "¿Cuál es el grado de dificultad que percibe en la asignatura?",
        1: "1 - Muy fácil",
        2: "2 - Fácil",
        3: "3 - Regular",
        4: "4 - Complicado",
        5: "5 - Muy complicado"
    },
    {
        "pregunta": "¿Cómo considera las herramientas y/o tecnologías aplicadas?",
        1: "1 - Obsoletas",
        2: "2 - Malas",
        3: "3 - Suficientes",
        4: "4 - Buenas",
        5: "5 - Excelentes"
    },
    {
        "pregunta": "¿Cómo considera las prácticas realizadas en las asignaturas?",
        1: "1 - Molestas",
        2: "2 - Aburridas",
        3: "3 - Mediocres",
        4: "4 - Interesantes",
        5: "5 - Muy buenas"
    }
]

# Lista de alumnos
alumnos = [
    "Adrián Hernández",
    "Eva González",
    "José Pat",
    "Aldahir Pech",
    "Kevin Rosas"
]

# Evaluaciones: estructura para guardar respuestas, apoyo para registrar variable, su contenido no se modifica
evaluaciones = {}

### FUNCIONES DE LA ESTRUCTURA
#
#
# Función que se encarga de limpiar la ventana, con cada pregunta
def limpiar(frame):
    list(map(lambda w: w.destroy(), frame.winfo_children()))

# Función que genera las vistas de los recursos de la ventana
def mostrar_preguntas(frame, aspecto_list, index, entradas):
    if index >= len(aspecto_list):  # Realiza una iteración interna para permitir crear los diferentes elementos
        return

    aspecto = aspecto_list[index]  # Toma el aspecto indicado con el valor de index

    tk.Label(frame, text=aspecto["pregunta"],
             font=("Arial", 12, "bold"), wraplength=600, justify="left").pack(pady=(10, 5))  # Aquí se construye la etiqueta de la pregunta

    list(map(
        lambda item: tk.Label(frame, text=item[1], font=("Arial", 10), wraplength=600, anchor="w").pack(anchor="w")
        if isinstance(item[0], int) else None,
        aspecto.items()
    ))  # Con este list se construyen etiquetas que despliegan las opciones que maneja la pregunta

    entrada = tk.Entry(frame, font=("Arial", 12), width=40)  # Se construye una entrada para texto en la cual se colocará la opción deseada
    entrada.pack(pady=(5, 20))
    entradas.append(entrada)

    mostrar_preguntas(frame, aspecto_list, index + 1, entradas)  # Se emplea recursividad para agregar el resto de preguntas en la ventana

# Función que se encarga de generar el cambio de las asignaturas y los alumnos
def evaluar(frame, alumnos, asignaturas, aspectos, evals, alumno_idx, asignatura_idx):
    limpiar(frame)  # Llamada a limpiar, para quitar los elementos que se encuentren y puedan estorbar

    if alumno_idx >= len(alumnos):  # Analiza si los alumnos ya pasaron y no queda ninguno
        mostrar_resultados(evals)  # Si ya no hay alumnos, entonces procede a mostrar resultados
        ventana.quit()  # Permite cerrar la ventana cuando el mensaje ya ha sido generado
        return

    alumno = alumnos[alumno_idx]  # Se asigna el alumno que corresponderá a evaluar
    asignatura_actual = asignaturas[asignatura_idx]  # Se asigna la asignatura sobre la cual se evaluará
    nombre_asignatura = asignatura_actual["asignatura"]  # Se extrae únicamente el nombre

    tk.Label(frame, text=f"Alumno: {alumno}", font=("Arial", 14, "bold"), bg="#7ab2d6").pack(pady=(5, 10))
    tk.Label(frame, text=f"Asignatura: {nombre_asignatura}", font=("Arial", 12), bg="#7ab2d6").pack(pady=(0, 10))
    # Se generan las etiquetas correspondientes para mostrar al alumno y la asignatura

    entradas = []  # Se registran las entradas obtenidas
    mostrar_preguntas(frame, aspectos, 0, entradas)  # Genera las preguntas por debajo de la asignatura

    def siguiente():  # Función que evaluará que las preguntas hayan sido respondidas y verificará que la entrada solo sea de 1 a 5 y almacenará los puntos
        if len(entradas) != 4:
            mb.showerror("Error", "Debe responder las 4 preguntas.")
            return

        r1 = entradas[0].get().strip()
        r2 = entradas[1].get().strip()
        r3 = entradas[2].get().strip()
        r4 = entradas[3].get().strip()

        if r1 not in ["1", "2", "3", "4", "5"] or \
        r2 not in ["1", "2", "3", "4", "5"] or \
        r3 not in ["1", "2", "3", "4", "5"] or \
        r4 not in ["1", "2", "3", "4", "5"]:
            mb.showerror("Error", "Todas las respuestas deben ser números del 1 al 5.")
            return

        puntaje_total = int(r1) + int(r2) + int(r3) + int(r4)

        nuevo_eval = evals.copy()
        nuevo_eval.setdefault(alumno, []).append(puntaje_total)

        siguiente_asignatura = asignatura_idx + 1
        if siguiente_asignatura < len(asignaturas):  # Comprobará si las asignaturas ya fueron evaluadas por un alumno
            evaluar(frame, alumnos, asignaturas, aspectos, nuevo_eval, alumno_idx, siguiente_asignatura)  # Si no han sido evaluadas todas, irá con la siguiente
        else:
            evaluar(frame, alumnos, asignaturas, aspectos, nuevo_eval, alumno_idx + 1, 0)  # Si ya las ha evaluado, seguirá con otro alumno

    tk.Button(frame, text="Continuar", command=siguiente,  # Se construye el botón que permitirá hacer el recorrido
              bg="#4a90e2", fg="white", font=("Arial", 12), padx=15, pady=8).pack(pady=(10, 5))

# Función que se encarga de generar los resultados que se desplegarán en una ventana de mensaje
def mostrar_resultados(evals):
    # Obtener nombres de asignaturas
    asignatura_nombres = list(map(lambda a: a["asignatura"], asignaturas))
    
    # Calcular sumas por asignatura
    sumas_por_asignatura = list(
        map(lambda i: sum(map(lambda alumno: evals[alumno][i], alumnos)),
            range(len(asignaturas)))
    )
    
    # Calcular promedios individuales
    promedios_individuales = list(map(lambda suma: round(suma / (len(alumnos) * len(aspectos)), 2),sumas_por_asignatura))
    # promedios_individuales = list(map(lambda suma: round(suma / (len(aspectos)), 2),sumas_por_asignatura))
    
    # Calcular valores agregados
    suma_total = reduce(lambda acc, suma: acc + suma, sumas_por_asignatura, 0)
    promedio_general = round(suma_total / (len(alumnos) * len(aspectos) * len(asignaturas)), 2)
    # promedio_general = round(suma_total / (len(aspectos) * len(asignaturas)), 2)
    
    # Totales individuales (suma cruda por asignatura)
    totales_individuales = sumas_por_asignatura
    
    # Valor máximo y mínimo
    maximo = reduce(lambda acc, suma: suma if suma > acc else acc, sumas_por_asignatura, 0)
    minimo = reduce(lambda acc, suma: suma if suma < acc else acc, sumas_por_asignatura, float('inf'))
    
    # Formatear resultados
    detalles = "\n".join(
        map(lambda i: (
            f"{asignatura_nombres[i]}:\n"
            f"  Promedio: {promedios_individuales[i]}\n"
            f"  Total: {totales_individuales[i]}\n"
            f"  Max: {max(map(lambda alumno: evals[alumno][i], alumnos))}\n"
            f"  Min: {min(map(lambda alumno: evals[alumno][i], alumnos))}"
        ), range(len(asignaturas)))
    )
    
    mb.showinfo("Resultados Finales",
               f"=== RESUMEN GENERAL ===\n"
               f"Promedio general: {promedio_general}\n"
               f"Total general: {suma_total}\n"
               f"Valor máximo: {maximo}\n"
               f"Valor mínimo: {minimo}\n\n"
               f"=== DETALLE POR ASIGNATURA ===\n{detalles}")

### Construcción de la Interfaz GUI
#
#
ventana = tk.Tk()  # Asigna para facilitar la identificación y dar atributos específicos
ventana.title("Evaluación de Asignaturas")  # Se otorga un título a la ventana
ventana.geometry("800x950")  # Se le asignan las dimensiones de la ventana
ventana.configure(bg="#7ab2d6")  # Se puede configurar la ventana para tener ciertas vistas, en este caso se cambió el color de fondo

frame_principal = tk.Frame(ventana, bg="#6a95e6")  # Se construye lo que es el panel o escena donde se generará la encuesta
frame_principal.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
 
# Inicia con la primera vista
evaluar(frame_principal, alumnos, asignaturas, aspectos, {}, 0, 0)

ventana.mainloop()  # Código que permite que la ventana trabaje y se puedan hacer los procesos en ventana