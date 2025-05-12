% Hechos
padre(juan, maria).
padre(juan, pedro).
padre(carlos, juan).
padre(adrian, evelin).
padre(adrian, victor).
padre(luis, adrian).
padre(jesus, sara).
padre(martin, luis).
padre(martin, jesus).

% Reglas
abuelo(X, Y) :- padre(X, Z), padre(Z, Y).
bisabuelo(X, Y) :- padre(X, Z), abuelo(Z, Y).