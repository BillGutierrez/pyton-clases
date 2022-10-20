#Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en dicha frase.

frase = input("ingrese una frase: ")
vocales = "aeiou"
contador = 0

for i in frase:
    if i in vocales:
        contador = contador+1

print("el numero de vocales es: ", contador)       