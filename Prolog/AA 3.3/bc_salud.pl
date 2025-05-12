% BASE DE CONOCIMIENTOS COMPLETA - ENFERMEDADES DIGESTIVAS (Versión estática)

% 1. CLASIFICACIÓN DE ENFERMEDADES POR TIPO
clasificacion(gastritis, inflamatoria).
clasificacion(ulcera_gastrica, estructural).
clasificacion(reflujo_gastroesofagico, funcional).
clasificacion(sindrome_intestino_irritable, funcional).
clasificacion(colitis_ulcerosa, inflamatoria).
clasificacion(enfermedad_crohn, inflamatoria).
clasificacion(estrenimiento_cronico, funcional).
clasificacion(diarrea_infecciosa, viral).
clasificacion(hepatitis_a, viral).
clasificacion(hepatitis_b_c, viral).
clasificacion(pancreatitis, inflamatoria).
clasificacion(enfermedad_celiaca, autoinmune).
clasificacion(intolerancia_lactosa, funcional).
clasificacion(apendicitis, inflamatoria).
clasificacion(cancer_colorrectal, estructural).

% 2. DESCRIPCIÓN DE TIPOS
descripcion_tipo(inflamatoria, 'Inflamación del tracto digestivo').
descripcion_tipo(funcional, 'Alteración en el funcionamiento normal').
descripcion_tipo(viral, 'Causada por agentes virales').
descripcion_tipo(autoinmune, 'El sistema inmunológico ataca al propio cuerpo').
descripcion_tipo(estructural, 'Daños anatómicos en los tejidos').

% 3. SÍNTOMAS POR ENFERMEDAD (Relaciones individuales)
% Gastritis
sintoma_de(dolor_abdominal, gastritis).
sintoma_de(nauseas, gastritis).
sintoma_de(vomito, gastritis).
sintoma_de(ardor_estomacal, gastritis).

% Úlcera gástrica
sintoma_de(dolor_abdomen_superior, ulcera_gastrica).
sintoma_de(acidez, ulcera_gastrica).
sintoma_de(perdida_apetito, ulcera_gastrica).

% Reflujo gastroesofágico
sintoma_de(acidez, reflujo_gastroesofagico).
sintoma_de(regurgitacion, reflujo_gastroesofagico).
sintoma_de(dolor_toracico, reflujo_gastroesofagico).

% Síndrome intestino irritable
sintoma_de(dolor_abdominal, sindrome_intestino_irritable).
sintoma_de(diarrea_alterna_estrenimiento, sindrome_intestino_irritable).
sintoma_de(gases, sindrome_intestino_irritable).

% Colitis ulcerosa
sintoma_de(diarrea_con_sangre, colitis_ulcerosa).
sintoma_de(dolor_abdominal, colitis_ulcerosa).
sintoma_de(fatiga, colitis_ulcerosa).

% Enfermedad de Crohn
sintoma_de(dolor_abdominal, enfermedad_crohn).
sintoma_de(diarrea_cronica, enfermedad_crohn).
sintoma_de(perdida_peso, enfermedad_crohn).

% Estreñimiento crónico
sintoma_de(defecacion_infrecuente, estrenimiento_cronico).
sintoma_de(heces_duras, estrenimiento_cronico).

% Diarrea infecciosa
sintoma_de(heces_liquidas, diarrea_infecciosa).
sintoma_de(fiebre, diarrea_infecciosa).
sintoma_de(dolor_abdominal, diarrea_infecciosa).

% Hepatitis A
sintoma_de(fatiga, hepatitis_a).
sintoma_de(ictericia, hepatitis_a).
sintoma_de(nauseas, hepatitis_a).

% Hepatitis B/C
sintoma_de(fatiga, hepatitis_b_c).
sintoma_de(ictericia, hepatitis_b_c).
sintoma_de(dolor_costado_derecho, hepatitis_b_c).

% Pancreatitis
sintoma_de(dolor_abdominal_intenso, pancreatitis).
sintoma_de(nauseas, pancreatitis).
sintoma_de(vomito, pancreatitis).

% Enfermedad celíaca
sintoma_de(diarrea, enfermedad_celiaca).
sintoma_de(distension_abdominal, enfermedad_celiaca).
sintoma_de(perdida_peso, enfermedad_celiaca).

% Intolerancia a la lactosa
sintoma_de(gases, intolerancia_lactosa).
sintoma_de(diarrea, intolerancia_lactosa).
sintoma_de(hinchazon_abdominal, intolerancia_lactosa).

% Apendicitis
sintoma_de(dolor_lado_derecho, apendicitis).
sintoma_de(fiebre, apendicitis).
sintoma_de(nauseas, apendicitis).

% Cáncer colorrectal
sintoma_de(sangrado_rectal, cancer_colorrectal).
sintoma_de(cambio_habitos_intestinales, cancer_colorrectal).
sintoma_de(perdida_peso, cancer_colorrectal).

% 4. TRATAMIENTOS (Relaciones individuales como con síntomas)
% Gastritis
tratamiento_para(antiacidos, gastritis).
tratamiento_para(inhibidores_bomba_protones, gastritis).
tratamiento_para(dieta_blanda, gastritis).

% Úlcera gástrica
tratamiento_para(antiacidos, ulcera_gastrica).
tratamiento_para(antibioticos_hpylori, ulcera_gastrica).
tratamiento_para(protectores_gastricos, ulcera_gastrica).

% Reflujo gastroesofágico
tratamiento_para(inhibidores_bomba_protones, reflujo_gastroesofagico).
tratamiento_para(elevar_cabecera, reflujo_gastroesofagico).
tratamiento_para(comidas_frecuentes_pequenas, reflujo_gastroesofagico).

% Síndrome intestino irritable
tratamiento_para(fibra_dietetica, sindrome_intestino_irritable).
tratamiento_para(antiespasmodicos, sindrome_intestino_irritable).
tratamiento_para(manejo_estres, sindrome_intestino_irritable).

% Colitis ulcerosa
tratamiento_para(aminosalicilatos, colitis_ulcerosa).
tratamiento_para(corticosteroides, colitis_ulcerosa).
tratamiento_para(inmunomoduladores, colitis_ulcerosa).

% Enfermedad de Crohn
tratamiento_para(antiinflamatorios, enfermedad_crohn).
tratamiento_para(inmunosupresores, enfermedad_crohn).
tratamiento_para(terapia_biologica, enfermedad_crohn).

% Estreñimiento crónico
tratamiento_para(aumento_fibra, estrenimiento_cronico).
tratamiento_para(laxantes_osmoticos, estrenimiento_cronico).
tratamiento_para(actividad_fisica, estrenimiento_cronico).

% Diarrea infecciosa
tratamiento_para(hidratacion, diarrea_infecciosa).
tratamiento_para(antidiarreicos, diarrea_infecciosa).
tratamiento_para(antibioticos_bacteriana, diarrea_infecciosa).

% Hepatitis A
tratamiento_para(reposo, hepatitis_a).
tratamiento_para(hidratacion, hepatitis_a).
tratamiento_para(evitar_alcohol, hepatitis_a).

% Hepatitis B/C
tratamiento_para(antivirales, hepatitis_b_c).
tratamiento_para(seguimiento_especializado, hepatitis_b_c).
tratamiento_para(vacunacion_hepatitis_b, hepatitis_b_c).

% Pancreatitis
tratamiento_para(ayuno, pancreatitis).
tratamiento_para(hidratacion_iv, pancreatitis).
tratamiento_para(analgesia, pancreatitis).

% Enfermedad celíaca
tratamiento_para(dieta_sin_gluten, enfermedad_celiaca).
tratamiento_para(suplementos_nutricionales, enfermedad_celiaca).

% Intolerancia a la lactosa
tratamiento_para(eliminacion_lacteos, intolerancia_lactosa).
tratamiento_para(enzima_lactasa, intolerancia_lactosa).

% Apendicitis
tratamiento_para(apendicectomia, apendicitis).
tratamiento_para(antibioticos, apendicitis).

% Cáncer colorrectal
tratamiento_para(cirugia, cancer_colorrectal).
tratamiento_para(quimioterapia, cancer_colorrectal).
tratamiento_para(radioterapia, cancer_colorrectal).

% 5. RECOMENDACIONES (Relaciones individuales como con síntomas)
% Gastritis
recomendacion_para(evitar_alcohol, gastritis).
recomendacion_para(evitar_cafe, gastritis).
recomendacion_para(comer_porciones_pequenas, gastritis).

% Úlcera gástrica
recomendacion_para(no_fumar, ulcera_gastrica).
recomendacion_para(evitar_aines, ulcera_gastrica).
recomendacion_para(manejar_estres, ulcera_gastrica).

% Reflujo gastroesofágico
recomendacion_para(no_acostarse_despues_comer, reflujo_gastroesofagico).
recomendacion_para(evitar_comidas_copiosas, reflujo_gastroesofagico).
recomendacion_para(evitar_grasas, reflujo_gastroesofagico).

% Síndrome intestino irritable
recomendacion_para(dieta_baja_fodmap, sindrome_intestino_irritable).
recomendacion_para(ejercicio_regular, sindrome_intestino_irritable).
recomendacion_para(evitar_estres, sindrome_intestino_irritable).

% Colitis ulcerosa
recomendacion_para(control_medico_regular, colitis_ulcerosa).
recomendacion_para(dieta_baja_fibra_brotes, colitis_ulcerosa).
recomendacion_para(evitar_estres, colitis_ulcerosa).

% Enfermedad de Crohn
recomendacion_para(suplementos_nutricionales, enfermedad_crohn).
recomendacion_para(evitar_tabaco, enfermedad_crohn).
recomendacion_para(descanso_adecuado, enfermedad_crohn).

% Estreñimiento crónico
recomendacion_para(ingesta_agua, estrenimiento_cronico).
recomendacion_para(consumir_frutas_con_piel, estrenimiento_cronico).
recomendacion_para(actividad_fisica, estrenimiento_cronico).

% Diarrea infecciosa
recomendacion_para(rehidratacion_oral, diarrea_infecciosa).
recomendacion_para(higiene_estricta, diarrea_infecciosa).
recomendacion_para(evitar_alimentos_contaminados, diarrea_infecciosa).

% Hepatitis A
recomendacion_para(vacunacion, hepatitis_a).
recomendacion_para(higiene_manos, hepatitis_a).
recomendacion_para(no_preparar_comida_otros, hepatitis_a).

% Hepatitis B/C
recomendacion_para(no_compartir_agujas, hepatitis_b_c).
recomendacion_para(sexo_seguro, hepatitis_b_c).
recomendacion_para(vacunacion_hepatitis_b, hepatitis_b_c).

% Pancreatitis
recomendacion_para(abstinencia_alcohol, pancreatitis).
recomendacion_para(dieta_baja_grasas, pancreatitis).
recomendacion_para(control_medico, pancreatitis).

% Enfermedad celíaca
recomendacion_para(leer_etiquetas, enfermedad_celiaca).
recomendacion_para(evitar_contaminacion_cruzada, enfermedad_celiaca).
recomendacion_para(control_nutricional, enfermedad_celiaca).

% Intolerancia a la lactosa
recomendacion_para(productos_deslactosados, intolerancia_lactosa).
recomendacion_para(suplementos_calcio, intolerancia_lactosa).
recomendacion_para(control_ingesta_lactosa, intolerancia_lactosa).

% Apendicitis
recomendacion_para(acudir_urgencias_dolor_derecho, apendicitis).
recomendacion_para(no_automedicarse, apendicitis).
recomendacion_para(seguimiento_postquirurgico, apendicitis).

% Cáncer colorrectal
recomendacion_para(tamizaje_despues_50, cancer_colorrectal).
recomendacion_para(dieta_rica_fibra, cancer_colorrectal).
recomendacion_para(evitar_tabaco_alcohol, cancer_colorrectal).

% 6. PREDICADOS DE CONSULTA (Actualizados)

% Obtener listas de síntomas/tratamientos/recomendaciones
sintomas_enfermedad(Enfermedad, Sintomas) :-
    findall(S, sintoma_de(S, Enfermedad), Sintomas).

tratamientos_enfermedad(Enfermedad, Tratamientos) :-
    findall(T, tratamiento_para(T, Enfermedad), Tratamientos).

recomendaciones_enfermedad(Enfermedad, Recomendaciones) :-
    findall(R, recomendacion_para(R, Enfermedad), Recomendaciones).

% Mostrar información completa
diagnostico(Enfermedad) :-
    clasificacion(Enfermedad, Tipo),
    descripcion_tipo(Tipo, DescTipo),
    sintomas_enfermedad(Enfermedad, Sintomas),
    tratamientos_enfermedad(Enfermedad, Tratamientos),
    recomendaciones_enfermedad(Enfermedad, Recomendaciones),
    
    format('~n=== ~w ===', [Enfermedad]),
    format('~nTipo: ~w (~w)', [Tipo, DescTipo]),
    format('~nSíntomas: ~w', [Sintomas]),
    format('~nTratamientos: ~w', [Tratamientos]),
    format('~nRecomendaciones: ~w~n', [Recomendaciones]).

% Consultas por tipo
enfermedades_por_tipo(Tipo, Enfermedades) :-
    findall(E, clasificacion(E, Tipo), Enfermedades).

% Búsqueda por síntoma
enfermedades_con_sintoma(Sintoma, Enfermedades) :-
    findall(E, sintoma_de(Sintoma, E), Enfermedades).

enfermedad_por_tipo(Tipo, Enfermedad) :-
    clasificacion(Enfermedad, Tipo).

sintoma_por_tipo(Tipo, Sintoma) :-
    clasificacion(Enfermedad, Tipo),
    sintoma_de(Sintoma, Enfermedad).

tratamiento_por_tipo(Tipo, Tratamiento) :-
    clasificacion(Enfermedad, Tipo),
    tratamiento_para(Tratamiento, Enfermedad).

recomendacion_por_tipo(Tipo, Recomendacion) :-
    clasificacion(Enfermedad, Tipo),
    recomendacion_para(Recomendacion, Enfermedad).

enfermedad_por_sintoma(Sintoma, Enfermedad) :-
    sintoma_de(Sintoma, Enfermedad).

tratamiento_por_sintoma(Sintoma, Tratamiento) :-
    sintoma_de(Sintoma, Enfermedad),
    tratamiento_para(Tratamiento, Enfermedad).

recomendacion_por_sintoma(Sintoma, Recomendacion) :-
    sintoma_de(Sintoma, Enfermedad),
    recomendacion_para(Recomendacion, Enfermedad).
