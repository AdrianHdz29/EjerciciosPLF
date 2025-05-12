:- dynamic si/1, no/1.  % Declarar los hechos dinámicos

:- write('ENFERMEDADES DIGESTIVAS'), nl, nl.

diagnostico :-
    diagnosticar(Enfermedad),
    write('DIAGNOSTICO:'), nl, nl,
    write('Enfermedad: '), write(Enfermedad), nl,
    write('Tipo(s):'), nl,
    mostrar_tipos(Enfermedad), nl,
    write('Sintomas: '), nl,
    sintomas(Enfermedad, Sintomas),
    write('- '), write(Sintomas), nl, nl,
    write('Tratamiento: '), nl,
    tratamiento(Enfermedad, Tratamiento),
    write('- '), write(Tratamiento), nl, nl,
    write('Recomendaciones: '), nl,
    recomendacion(Enfermedad, Recomendacion),
    write('- '), write(Recomendacion), nl,
    undo.

% Diagnosticar la enfermedad digestiva
diagnosticar(gastritis) :- gastritis , !.
diagnosticar(ulcera_gastrica) :- ulcera_gastrica , !.
diagnosticar(reflujo_gastroesofagico) :- reflujo_gastroesofagico , !.
diagnosticar(sindrome_del_intestino_irritable) :- sindrome_del_intestino_irritable , !.
diagnosticar(colitis_ulcerosa) :- colitis_ulcerosa , !.
diagnosticar(enfermedad_de_crohn) :- enfermedad_de_crohn , !.
diagnosticar(estrenimiento_cronico) :- estrenimiento_cronico , !.
diagnosticar(diarrea_infecciosa) :- diarrea_infecciosa , !.
diagnosticar(hepatitis_a) :- hepatitis_a , !.
diagnosticar(hepatitis_b_y_c) :- hepatitis_b_y_c , !.
diagnosticar(pancreatitis) :- pancreatitis , !.
diagnosticar(enfermedad_celiaca) :- enfermedad_celiaca , !.
diagnosticar(intolerancia_lactosa) :- intolerancia_lactosa , !.
diagnosticar(apendicitis) :- apendicitis , !.
diagnosticar(cancer_colorrectal) :- cancer_colorrectal , !.
diagnosticar(sin_identificar).

% Reglas identificadas
gastritis :- inflamatoria,
    preguntar(dolor_abdominal),
    preguntar(nauseas),
    preguntar(vomito),
    preguntar(ardor).
ulcera_gastrica :- estructural,
    preguntar(dolor_abdomen_superior),
    preguntar(acidez),
    preguntar(perdida_apetito).
reflujo_gastroesofagico :- funcional,
    preguntar(acidez),
    preguntar(regurgitacion),
    preguntar(dolor_toracico).
sindrome_del_intestino_irritable :- funcional,
    preguntar(dolor_abdominal),
    preguntar(diarrea_o_estrenimiento),
    preguntar(gases).
colitis_ulcerosa :- inflamatoria,
    preguntar(diarrea_con_sangre),
    preguntar(dolor_abdominal),
    preguntar(fatiga).
enfermedad_de_crohn :- inflamatoria,
    preguntar(dolor_abdominal),
    preguntar(diarrea_cronica),
    preguntar(perdida_de_peso).
estrenimiento_cronico :- funcional,
    preguntar(poca_defecacion),
    preguntar(heces_duras).
diarrea_infecciosa :- viral,
    preguntar(heces_liquidas_frecuentes),
    preguntar(fiebre),
    preguntar(dolor_abdominal).
hepatitis_a :- viral,
    preguntar(fatiga),
    preguntar(ictericia),
    preguntar(nauseas),
    preguntar(dolor_hepatico).
hepatitis_b_y_c :- viral,
    preguntar(fatiga),
    preguntar(ictericia),
    preguntar(dolor_costado_derecho).
pancreatitis :- inflamatoria,
    preguntar(dolor_abdominal),
    preguntar(nauseas),
    preguntar(vomito).
enfermedad_celiaca :- autoinmune,
    preguntar(diarrea),
    preguntar(distencion_abdominal),
    preguntar(perdida_de_peso).
intolerancia_lactosa :- funcional, autoinmune,
    preguntar(gases),
    preguntar(diarrea),
    preguntar(hinchazon_por_lacteos).
apendicitis :- inflamatoria, estructural,
    preguntar(dolor_abdominal_lado_derecho),
    preguntar(fiebre),
    preguntar(nauseas).
cancer_colorrectal :- estructural,
    preguntar(sangrado_rectal),
    preguntar(habitos_intestinales_irregulares),
    preguntar(perdida_de_peso).

% Clasificacion por tipo
inflamatoria :- preguntar(incomodidad_estomacal), !.
inflamatoria :- preguntar(sensacion_de_inflamacion).

funcional :- preguntar(molestias_digestivas), !.
funcional :- preguntar(estres), !.
funcional :- preguntar(actividad_anormal_digestiva).

autoinmune :- preguntar(problemas_con_lacteos), !.
autoinmune :- preguntar(problemas_con_gluten), !.
autoinmune :- preguntar(mejora_con_cambio_de_dieta).

viral :- preguntar(brotes_comunes_por_actividades), !.
viral :- preguntar(aparicion_subita_de_sintomas).

estructural :- preguntar(lesiones), !.
estructural :- preguntar(ulceras), !.
estructural :- preguntar(tumores), !.
estructural :- preguntar(malformaciones), !.
estructural :- preguntar(sangrado), !.
estructural :- preguntar(disminucion_peso), !.
estructural :- preguntar(dolor_persistente).

% Hechos para descripciones de tipos
tipo(inflamatoria, 'Inflamación del revestimiento digestivo').
tipo(funcional, 'Altera el funcionamiento').
tipo(autoinmune, 'El sistema inmune reacciona contra el propio cuerpo o alimentos comunes').
tipo(viral, 'Causada por microorganismos').
tipo(estructural, 'Dañan el revestimiento y el tubo digestivo').

% Asociación de enfermedades con sus tipos
tipos(gastritis, [inflamatoria]).
tipos(ulcera_gastrica, [estructural]).
tipos(reflujo_gastroesofagico, [funcional]).
tipos(sindrome_del_intestino_irritable, [funcional]).
tipos(colitis_ulcerosa, [inflamatoria]).
tipos(enfermedad_de_crohn, [inflamatoria]).
tipos(estrenimiento_cronico, [funcional]).
tipos(diarrea_infecciosa, [viral]).
tipos(hepatitis_a, [viral]).
tipos(hepatitis_b_y_c, [viral]).
tipos(pancreatitis, [inflamatoria]).
tipos(enfermedad_celiaca, [autoinmune]).
tipos(intolerancia_lactosa, [funcional, autoinmune]).
tipos(apendicitis, [inflamatoria, estructural]).
tipos(cancer_colorrectal, [estructural]).

mostrar_tipos(Enfermedad) :-
    tipos(Enfermedad, Lista),
    mostrar_tipos_lista(Lista).

mostrar_tipos_lista([]).
mostrar_tipos_lista([Tipo|Resto]) :-
    tipo(Tipo, Descripcion),
    format('- ~w: ~w~n', [Tipo, Descripcion]),
    mostrar_tipos_lista(Resto).

% Sintomas
sintomas(gastritis, ['Dolor abdominal', 'Náuseas', 'Vómitos', 'Sensación de ardor']).
sintomas(ulcera_gastrica, ['Dolor en la parte superior del abdomen', 'Acidez', 'Pérdida de apetito']).
sintomas(reflujo_gastroesofagico, ['Acidez', 'Regurgitación', 'Dolor torácico']).
sintomas(sindrome_del_intestino_irritable, ['Dolor abdominal', 'Diarrea o estreñimiento', 'Gases']).
sintomas(colitis_ulcerosa, ['Diarrea con sangre', 'Dolor abdominal', 'Fatiga']).
sintomas(enfermedad_de_crohn, ['Dolor abdominal', 'Diarrea crónica', 'Pérdida de peso']).
sintomas(estrenimiento_cronico, ['Menos de tres evacuaciones semanales', 'Heces duras']).
sintomas(diarrea_infecciosa, ['Heces líquidas frecuentes', 'Fiebre', 'Dolor abdominal']).
sintomas(hepatitis_a, ['Fatiga', 'Ictericia', 'Náuseas', 'Dolor hepático']).
sintomas(hepatitis_b_y_c, ['Fatiga', 'Ictericia', 'Dolor en el costado derecho']).
sintomas(pancreatitis, ['Dolor abdominal intenso', 'Náuseas', 'Vómitos']).
sintomas(enfermedad_celiaca, ['Diarrea', 'Distensión abdominal', 'Pérdida de peso']).
sintomas(intolerancia_lactosa, ['Gases', 'Diarrea', 'Hinchazón después de consumir lácteos']).
sintomas(apendicitis, ['Dolor abdominal intenso en el lado derecho', 'Fiebre', 'Náuseas']).
sintomas(cancer_colorrectal, ['Sangrado rectal', 'Cambio en hábitos intestinales', 'Pérdida de peso']).

% Tratamientos
tratamiento(gastritis, 'Antiácidos, inhibidores de la bomba de protones (omeprazol), antibióticos si hay Hecobacter pylori').
tratamiento(ulcera_gastrica, 'Antiácidos, omeprazol, erradicación de Hecobacter pylori').
tratamiento(reflujo_gastroesofagico, 'Inhibidores de la bomba de protones, cambios dietéticos').
tratamiento(sindrome_del_intestino_irritable, 'Antiespasmódicos, fibra, manejo del estrés').
tratamiento(colitis_ulcerosa, 'Aminosalicilatos, corticosteroides, inmunosupresores').
tratamiento(enfermedad_de_crohn, 'Corticoides, inmunomoduladores, cirugía en casos severos').
tratamiento(estrenimiento_cronico, 'Laxantes, fibra, hidratación').
tratamiento(diarrea_infecciosa, 'Hidratación oral, antibióticos si hay infección bacteriana').
tratamiento(hepatitis_a, 'Reposo, hidratación, dieta saludable').
tratamiento(hepatitis_b_y_c, 'Antivirales (interferón, entecavir, sofosbuvir)').
tratamiento(pancreatitis, 'Hospitalización, ayuno, hidratación intravenosa').
tratamiento(enfermedad_celiaca, 'Dieta estricta sin gluten').
tratamiento(intolerancia_lactosa, 'Evitar productos con lactosa, enzima lactasa').
tratamiento(apendicitis, 'Apendicectomía').
tratamiento(cancer_colorrectal, 'Cirugía, quimioterapia, radioterapia').

% Recomendaciones
recomendacion(gastritis, 'Evitar alcohol, tabaco, café, comidas picantes; comer en horarios regulares').
recomendacion(ulcera_gastrica, 'Evitar el estrés, no automedicarse con AINEs, dieta suave').
recomendacion(reflujo_gastroesofagico, 'Elevar la cabecera al dormir, no acostarse tras comer, evitar alimentos grasos').
recomendacion(sindrome_del_intestino_irritable, 'Dieta baja en FODMAP, ejercicio regular, evitar cafeína y alcohol').
recomendacion(colitis_ulcerosa, 'Dieta baja en fibra durante brotes, seguimiento médico, evitar el estrés').
recomendacion(enfermedad_de_crohn, 'Controlar el estrés, dieta personalizada, evitar el tabaco').
recomendacion(estrenimiento_cronico, 'Aumentar la actividad física, consumir frutas, verduras y agua').
recomendacion(diarrea_infecciosa, 'Lavado de manos, evitar alimentos contaminados, reposo').
recomendacion(hepatitis_a, 'Vacunación, higiene alimentaria, evitar alcohol').
recomendacion(hepatitis_b_y_c, 'No compartir agujas o cepillos, usar protección sexual, seguimiento médico').
recomendacion(pancreatitis, 'Evitar alcohol, dieta baja en grasas, control médico').
recomendacion(enfermedad_celiaca, 'Leer etiquetas, evitar contaminación cruzada, seguimiento nutricional').
recomendacion(intolerancia_lactosa, 'Usar alternativas vegetales o deslactosadas, dieta equilibrada en calcio').
recomendacion(apendicitis, 'Acudir pronto al médico ante síntomas, evitar automedicarse').
recomendacion(cancer_colorrectal, 'Tamizaje después de los 50 años, dieta rica en fibra, evitar tabaco y alcohol').

% Preguntas para identificar
consultar(Pregunta) :-
    write('¿Presenta este sintoma: '),
    write(Pregunta), write('?  '),
    read(Respuesta), nl,
    ((Respuesta == si ; Respuesta == s) 
        -> asserta(si(Pregunta)) ; assertz(no(Pregunta)),
        fail).

preguntar(S) :- (si(S) -> true ; (no(S) -> fail ; consultar(S))).

undo :- retract(si(_)), fail.
undo :- retract(no(_)), fail.
undo.