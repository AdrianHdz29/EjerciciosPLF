% Síntomas comunes
sintoma_comun(acidez).
sintoma_comun(dolor_abdominal).
sintoma_comun(nauseas).
sintoma_comun(indigestion).

% Síntomas específicos por tipo
sintoma_especifico(aguda, vomito).
sintoma_especifico(aguda, fiebre_leve).

sintoma_especifico(cronica, malestar_despues_comer).
sintoma_especifico(cronica, fatiga).

sintoma_especifico(bacteriana, mal_aliento).
sintoma_especifico(bacteriana, ulceras).

sintoma_especifico(autoinmune, debilidad).
sintoma_especifico(autoinmune, hormigueo).



tratamiento(aguda, 'Antiácidos y reposo').
tratamiento(cronica, 'Inhibidores de bomba de protones').
tratamiento(bacteriana, 'Antibióticos (amoxicilina + claritromicina)').
tratamiento(autoinmune, 'Suplementos de vitamina B12').



% Tiene gastritis solo si tiene TODOS los síntomas comunes
tiene_gastritis(Paciente) :-
    forall(sintoma_comun(S), sintoma(Paciente, S)).

% Tiene un tipo específico solo si además tiene TODOS los síntomas específicos de ese tipo
tiene_tipo_gastritis(Paciente, Tipo) :-
    tiene_gastritis(Paciente),
    sintoma_especifico(Tipo, _),
    forall(sintoma_especifico(Tipo, S), sintoma(Paciente, S)), !.

% Solo si tiene gastritis y un tipo confirmado, se da tratamiento
tratamiento_recomendado(Paciente, Tratamiento) :-
    tiene_tipo_gastritis(Paciente, Tipo),
    tratamiento(Tipo, Tratamiento), !.




sintoma(adrian, acidez).
sintoma(adrian, dolor_abdominal).
sintoma(adrian, nauseas).
sintoma(adrian, indigestion).
sintoma(adrian, mal_aliento).
sintoma(adrian, ulceras).

sintoma(victor, acidez).
sintoma(victor, dolor_abdominal).
sintoma(victor, nauseas).
sintoma(victor, indigestion).
sintoma(victor, vomito).
sintoma(victor, fiebre_leve).

sintoma(eva, acidez).
sintoma(eva, indigestion).
