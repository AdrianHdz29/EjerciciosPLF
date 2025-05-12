:- dynamic si/1, no/1.  % Declarar los hechos dinámicos

identificar :- 
    analizar(Animal),
    write('El animal es: '),
    write(Animal), nl, undo.

% Analizar el animal doméstico
analizar(perro) :- perro, !.
analizar(gato) :- gato, !.
analizar(loro) :- loro, !.
analizar(tortuga) :- tortuga, !.
analizar(conejo) :- conejo, !.
analizar(hamster) :- hamster, !.
analizar(desconocido).

% Reglas de identificación
perro :- mamifero, carnivoro, verificar(ladra), verificar(tiene_pelo).
gato :- mamifero, carnivoro, verificar(maulla), verificar(tiene_pelo).
loro :- ave, herviboro, verificar(habla), verificar(vuela), verificar(tiene_plumas).
tortuga :- reptil, herviboro, verificar(sin_sonido), verificar(tiene_escamas).
conejo :- mamifero, herviboro, verificar(chilla), verificar(tiene_pelo).
hamster :- mamifero, herviboro, verificar(chirria), verificar(tiene_pelo).

% Clasificación de las reglas
mamifero :- verificar(tiene_pelo), !.
mamifero :- verificar(da_leche).

ave :- verificar(tiene_plumas), !.
ave :- verificar(vuela), verificar(pone_huevos).

reptil :- verificar(tiene_escamas), !.
reptil :- verificar(pone_huevos), verificar(muda_piel).

carnivoro :- verificar(come_carne), !.
carnivoro :- verificar(colmillos), verificar(ojos_de_frente).

herviboro :- verificar(come_plantas), !.
herviboro :- verificar(dientes_planos), verificar(ojos_laterales).

% Preguntas para identificar
quest(Pregunta) :-
    write('¿El animal tiene los siguientes atributos: '),
    write(Pregunta), write('?  '),
    read(Respuesta), nl,
    ((Respuesta == si ; Respuesta == s) 
        -> asserta(si(Pregunta)) ; assertz(no(Pregunta)),
        fail).

verificar(S) :- (si(S) -> true ; (no(S) -> fail ; quest(S))).

undo :- retract(si(_)), fail.
undo :- retract(no(_)), fail.
undo.
