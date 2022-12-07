"""Escriba un programa que permita crear una lista de palabras (que puede ser vacía). 
Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras
para crear la lista. Por último, el programa tiene que escribir la lista."""


numero = int(input("Dígame cuántas palabras tiene la lista: "))
if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)