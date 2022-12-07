#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista y la muestre por pantalla.

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
puntaje = []
for materia in materias:
    puntaje = input("¿Qué nota has sacado en " + materia + "?")
    puntaje.append(puntaje)
for i in range(len(materias)):
    print("En " + materias[i] + " has sacado " + puntaje[i])