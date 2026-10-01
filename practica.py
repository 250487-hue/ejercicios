def mostrar_encabezado_escuela ():
    print("--------------------------------------------")
    print("---Universidad Tecnologica de Xicotepec de Juarez----")
    

def obtener_nota_minima_aprobatoria():
    return 6

def evaluar_rendimiento(nota_final):
    if nota_final < 7 and nota_final <=9: 
        return "Reprobado"
    elif nota_final >=7 and nota_final <=9:
        return "Aprovado"
    else:
        return "Excelente"

def calcular_promedio_ponderado(nota_examenes, nota_tareas):
   calificacion_final = (nota_examenes*0.70)+(nota_tareas*0.30)
   return round (calificacion_final,1)


def generar_boleta (nombre_alumno, nota_examenes,nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)
    
    if nota_final < nota_minima:
        extraordinario = "Si"
    else:
        extraordinario = "No"

    print(f"Alunmo:{nombre_alumno}")
    print(f"Nota Final Ponderada:{nota_final}")
    print(f"Estado Academico:{estado}")
    print(f"Iras a extraordinario? La respuesta es........{extraordinario}")
    print("......................................................")

mostrar_encabezado_escuela()
generar_boleta("Pedro ", 8.5, 9.0)