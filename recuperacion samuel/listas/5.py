"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""


materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobadas = []
for i in materias:
    print("¿Qué nota has sacado en ",i,"?")
    score = float(input())
    if score >= 5:
        aprobadas.append(i)

for m in aprobadas:
    materias.remove(m)
print("Tienes que repetir ",materias)