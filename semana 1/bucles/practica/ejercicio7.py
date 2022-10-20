palabra1 = input("ingrese palabra 1: ")
palabra2 = input("ingrese palabra 2: ")

for palab in palabra1:
    if palab in ("a","e","i","o","u"):
        continue
    
print(palab)