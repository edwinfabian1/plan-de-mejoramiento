edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
def edades(edad):
    if edad < 4:
        precio = 0
    elif edad <= 18:
        precio = 4
    else:
        precio = 10
    return "El precio de la entrada es", precio, "€."
# Mostrar precio
print(edades(edad))
