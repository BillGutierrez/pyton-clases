lado1 = int(input("ingrese lado1: "))
lado2 = int(input("ingrese lado2: "))
lado3 = int(input("ingrese lado3: "))

if lado1 == lado2 == lado3:
    print("Es un triangulo equilatero")
elif lado1 != lado2 != lado3:
    print("es un triangulo escaleno")
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    print("es un triangulo isoseles")