import random

# Quiero que un entero
number = random.randint(1, 1000)
print("trampa", number)
cont=0
while True:
    num = int(input("Ingrese un numero: "))

    if num == number:
        print("Adivinaste el numero", num)
        print("Intentos: ", cont)
        break
    elif num < number:
        print("Debes ingresar un numero mayor")
        cont += 1
    else:
        print("Debes ingresar un numero menor")
        cont += 1