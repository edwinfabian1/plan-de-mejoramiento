'''Genere una lista con numeros al azar y elevelos al cuadrado'''

import random

def al_cuadrado(lista):
    al_cuadrado = []
    i = 0
    while i < len(lista):
       al_cuadrado.append(lista[i]**2)
       i += 1
    return al_cuadrado

lista_inicial = [random.randint(1,50) for i in range (5)]
print(lista_inicial)

for i in al_cuadrado(lista_inicial):
    print(i)
