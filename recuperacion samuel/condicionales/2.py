"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos superiores a 1000 € mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
y muestre por pantalla si el usuario tiene que tributar o no."""

edad = int(input("¿Cuál es tu edad? "))
ingreso = float(input("¿Cuales son tus ingresos mensuales?"))
if edad > 18 and ingreso >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")