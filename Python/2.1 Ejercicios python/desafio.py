# Sombrero seleccionador ISC 🎩

# Inicialización de puntajes
redes = 0
bases_datos = 0
desarrollo_software = 0
programacion_hardware = 0
modelado_3d = 0
gestion_proyectos = 0

print('===============') 
print('El sombrero seleccionador ISC 🎩') 
print('===============') 

# Pregunta 1
print('\nP1) ¿Qué tipo de problemas disfrutas resolver?')
print('  1) Conectividad y comunicación entre dispositivos')  # Redes
print('  2) Organización y manejo de grandes volúmenes de datos')  # Bases de Datos
print('  3) Desarrollo de aplicaciones y software')  # Desarrollo de Software
print('  4) Diseño de hardware y optimización de dispositivos')  # Programación Hardware
print('  5) Creación de modelos y animaciones en 3D')  # Modelado 3D
print('  6) Planificación y coordinación de proyectos')  # Gestión de Proyectos
respuesta = int(input('Ingresa tu respuesta (1-6): '))
if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    programacion_hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2

# Pregunta 2
print('\nP2) ¿Cuál de estas actividades te parece más interesante?')
print('  1) Configurar servidores y routers')  
print('  2) Diseñar esquemas de bases de datos eficientes')  
print('  3) Programar nuevas funcionalidades en aplicaciones')  
print('  4) Diseñar circuitos electrónicos')  
print('  5) Modelar objetos en un entorno digital')  
print('  6) Coordinar equipos y tiempos en proyectos de software')  
respuesta = int(input('Ingresa tu respuesta (1-6): '))
if respuesta == 1:
    redes += 3
elif respuesta == 2:
    bases_datos += 3
elif respuesta == 3:
    desarrollo_software += 3
elif respuesta == 4:
    programacion_hardware += 3
elif respuesta == 5:
    modelado_3d += 3
elif respuesta == 6:
    gestion_proyectos += 3

# Pregunta 3
print('\nP3) ¿En qué ambiente de trabajo te sentirías más cómodo?')
print('  1) Administrando redes y servidores')  
print('  2) Organizando información para mejorar decisiones')  
print('  3) Desarrollando software en un equipo de programación')  
print('  4) Trabajando con microcontroladores y hardware')  
print('  5) Creando gráficos y simulaciones visuales')  
print('  6) Dirigiendo proyectos y asegurando su cumplimiento')  
respuesta = int(input('Ingresa tu respuesta (1-6): '))
if respuesta == 1:
    redes += 4
elif respuesta == 2:
    bases_datos += 4
elif respuesta == 3:
    desarrollo_software += 4
elif respuesta == 4:
    programacion_hardware += 4
elif respuesta == 5:
    modelado_3d += 4
elif respuesta == 6:
    gestion_proyectos += 4

# Pregunta 4
print('\nP4) ¿Qué herramienta te gustaría dominar?')
print('  1) Wireshark o Packet Tracer')  
print('  2) MySQL o PostgreSQL')  
print('  3) Python o Java')  
print('  4) Arduino o Raspberry Pi')  
print('  5) Blender o Maya')  
print('  6) Jira o Trello')  
respuesta = int(input('Ingresa tu respuesta (1-6): '))
if respuesta == 1:
    redes += 3
elif respuesta == 2:
    bases_datos += 3
elif respuesta == 3:
    desarrollo_software += 3
elif respuesta == 4:
    programacion_hardware += 3
elif respuesta == 5:
    modelado_3d += 3
elif respuesta == 6:
    gestion_proyectos += 3

# Pregunta 5
print('\nP5) ¿Cuál de estos roles te llama más la atención?')
print('  1) Ingeniero en redes y telecomunicaciones')  
print('  2) Administrador de bases de datos')  
print('  3) Desarrollador de software')  
print('  4) Ingeniero en sistemas embebidos')  
print('  5) Diseñador y animador 3D')  
print('  6) Gerente de proyectos tecnológicos')  
respuesta = int(input('Ingresa tu respuesta (1-6): '))
if respuesta == 1:
    redes += 5
elif respuesta == 2:
    bases_datos += 5
elif respuesta == 3:
    desarrollo_software += 5
elif respuesta == 4:
    programacion_hardware += 5
elif respuesta == 5:
    modelado_3d += 5
elif respuesta == 6:
    gestion_proyectos += 5

# Pregunta 6
print('\nP6) ¿Cómo te gustaría impactar en la industria tecnológica?')
print('  1) Mejorando la conectividad global')  
print('  2) Gestionando datos de manera eficiente')  
print('  3) Creando software innovador')  
print('  4) Desarrollando dispositivos inteligentes')  
print('  5) Diseñando experiencias visuales impresionantes')  
print('  6) Liderando proyectos de alto impacto')  
respuesta = int(input('Ingresa tu respuesta (1-6): '))
if respuesta == 1:
    redes += 4
elif respuesta == 2:
    bases_datos += 4
elif respuesta == 3:
    desarrollo_software += 4
elif respuesta == 4:
    programacion_hardware += 4
elif respuesta == 5:
    modelado_3d += 4
elif respuesta == 6:
    gestion_proyectos += 4

# Mostrar resultados
print("\nResultados:")
print(f"Redes: ", redes)
print(f"Bases de Datos: ", bases_datos)
print(f"Desarrollo de Software: ", desarrollo_software)
print(f"Programación Hardware: ", programacion_hardware)
print(f"Modelado 3D: ",modelado_3d)
print(f"Gestión de Proyectos: ", gestion_proyectos)

# Determinar la mejor rama con if-elif-else
if (redes >= bases_datos and redes >= desarrollo_software and 
    redes >= programacion_hardware and redes >= modelado_3d and redes >= gestion_proyectos):
    print("\n✨ Tu área recomendada es: Redes ✨")
elif (bases_datos >= desarrollo_software and bases_datos >= programacion_hardware and 
      bases_datos >= modelado_3d and bases_datos >= gestion_proyectos):
    print("\n✨ Tu área recomendada es: Bases de Datos ✨")
elif (desarrollo_software >= programacion_hardware and desarrollo_software >= modelado_3d and 
      desarrollo_software >= gestion_proyectos):
    print("\n✨ Tu área recomendada es: Desarrollo de Software ✨")
elif (programacion_hardware >= modelado_3d and programacion_hardware >= gestion_proyectos):
    print("\n✨ Tu área recomendada es: Programación Hardware ✨")
elif (modelado_3d >= gestion_proyectos):
    print("\n✨ Tu área recomendada es: Modelado 3D ✨")
else:
    print("\n✨ Tu área recomendada es: Gestión de Proyectos de Software ✨")