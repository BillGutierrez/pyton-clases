#Escribir un programa que muestre la sumatoria de todos los múltiplos de 3 encontrados entre el 0 y el 100.

lista = []
for i in range(0,100,3):
    lista.append(i)
print(sum(lista))