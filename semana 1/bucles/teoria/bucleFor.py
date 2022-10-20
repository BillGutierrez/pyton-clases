# numeros = [1, 2, 3, 4, 5]

# for i in numeros:
#     if i % 2 == 0:
#         print("Par ", i)
#     else:
#         print("Impar ", i)

# nombre = "juanito perez"

# for i in nombre:
#     print(i)


#(  `  ) comilla invertida


# for index in range(10, 51):
#     if index % 2 == 0:
#         print(index, " par")
#     else:
#         print(index, " impar")

# numero = int(input("Ingrse un numero: "))

# for i in range(0,13):
#     print(f"{i} x {numero} = ", i*numero)

# numero = 2
# suma = 0
# while numero != 0:
#     numero = int(input("ingrese numero: "))
#     suma += numero
    
# print("la suma es: ",suma)

positivos = []
negativos = []

while True:
    numero = int(input("ingrese un numero: "))
    if numero > 0:
        positivos.append(numero)
    elif numero < 0:
        negativos.append(numero)
    else:
        break
print(f"la suma de positivos es: {sum(positivos)}")
print(f"la suma de negativos es: {sum(negativos)}")
print("la cantidad numero ingresados es: " ,len(positivos)+len(negativos))