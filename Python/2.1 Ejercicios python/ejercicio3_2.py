import random

pregunta = input('pregunta:     ')

numero_aleatorio = random.randint(1, 9)

if numero_aleatorio == 1:
    respuesta = 'Si - definitivamente'
elif numero_aleatorio == 2:
    respuesta = 'Está decidido'
elif numero_aleatorio == 3:
    respuesta = 'Sin duda'
elif numero_aleatorio == 4:
    respuesta = 'Respuesta confusa, intenta de nuevo'
elif numero_aleatorio == 5:
    respuesta = 'Pregunta más tarde'
elif numero_aleatorio == 6:
    respuesta = 'Mejor no te digo'
elif numero_aleatorio == 7:
    respuesta = 'Mis fuentes dicen que no'
elif numero_aleatorio == 8:
    respuesta = 'No parece bueno'
elif numero_aleatorio == 9:
    respuesta = 'Muy dudoso'
else:
    respuesta = 'error'

print('Bola mágica:    ' + respuesta)