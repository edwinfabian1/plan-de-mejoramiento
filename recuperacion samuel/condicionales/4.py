#Escribir un programa que pida al usuario dos números y devuelva su división.
#Si el usuario no introduce números debe devolver un aviso de error y si el divisor es cero también.

n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisior: "))
if m == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(n/m)