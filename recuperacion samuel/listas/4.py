#Escribir un programa que almacene en una lista los números del 1 al 10 
#y los muestre por pantalla en orden inverso separados por comas.

numbers = [i for i in range (1,11)]
print (numbers)
for i in range(1, 11):
    print(numbers[-i], end=", ")