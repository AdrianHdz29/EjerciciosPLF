:- set_prolog_flag(encoding, utf8).

% Arbol familiar
mujer(victoria).
mujer(rosario).
mujer(rosenda).
mujer(maricela).
mujer(valeria).
mujer(dana).
mujer(paola).

madre(victoria, rosario).
madre(victoria, rosenda).
madre(victoria, maricela).
madre(rosario, valeria).
madre(rosenda, dana).
madre(rosenda, paola).


% Datos de empleados
empleado(juan, 35, ingeniero).
empleado(maria, 28, analista).
empleado(pedro, 40, gerente).

% Crear regla para consultar empleados menores a 30 años
joven(Persona):- empleado(Persona, Edad, _), Edad < 30.

% Pregunta y respuesta
saludo_respuesta(Saludo):-
    member(Saludo, ["Hola", "¿Cómo estás?", "Buenos días", "¿Qué tal?"]),
    responder_saludo(Saludo).

% Regla auxiliar para responder a saludos específicos
responder_saludo("Hola"):-
    write('¡Hola! ¿En qué puedo ayudarte?'), nl.
responder_saludo("¿Cómo estás?"):-
    write('Estoy bien, gracias por preguntar.'), nl.
responder_saludo("Buenos días"):-
    write('¡Buenos días! ¿Cómo puedo ayudarte hoy?'), nl.
responder_saludo("¿Qué tal?"):-
    write('Todo bien, ¿y tú?'), nl.
responder_saludo(_):-
    write('Lo siento, no entendí tu saludo.'), nl.