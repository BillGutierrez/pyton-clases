#Requerir al usuario que ingrese un número entero positivo e imprimir 
#todos los números correlativos entre el ingresado por el usuario y 
#uno menos del doble del mismo.

numero = int(input("Ingrese un numero: "))

for i in range(numero,2*numero):
    print(i)