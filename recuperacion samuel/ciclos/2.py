#Escriba un programa que pida la anchura 
#de un triángulo y lo dibuje con caracteres producto (*):
anchura = int(input("Anchura del triángulo: "))

for i in range(1, anchura + 1):
    for j in range(i):
        print("* ", end="")
    print()

for i in range(1, anchura):
    for j in range(anchura - i):
        print("* ", end="")
    print()