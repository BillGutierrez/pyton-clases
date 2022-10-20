años = int(input("ingrese años: "))
genero = input("ingrese genero: ")

if años > 25 and genero == "mujer":
    print("descuento de 23%")
elif años > 25 and genero == "varon":
    print("descuento de 20%")    
elif años > 20:
    print("descuento de 17%")
elif años > 10:
    print("descuento de 5%")
  