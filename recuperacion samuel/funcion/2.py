"""En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación
comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4. o 0.6,
pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad
de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel."""

puntos = float(input("Introduce tu puntuación: "))

bonificacion = 2400
inaceptable = 0
aceptable = 50
meritorio = 100

def calificacion(puntos):
    if puntos >= inaceptable:
        nivel = "Inaceptable"
    elif puntos >= aceptable:
        nivel = "Aceptable"
    elif puntos >= meritorio:
        nivel = "Meritorio"
    else:
        nivel = ""
    # Mostrar nivel de rendimiento
    if nivel == "":
        print("Esta puntuación no es válida")
    else:
        print("Tu nivel de rendimiento es",nivel)
        print("Te corresponde cobrar $",puntos * bonificacion)

calificacion(puntos)