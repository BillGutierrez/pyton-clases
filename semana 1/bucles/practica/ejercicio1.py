a = float(input("ingrese un numero: "))
b = float(input("ingrese otr numero: "))
oper = float(input("ingrese un operador: "))

if oper == "+":
    print(a+b)
elif oper == "-":
    print(a-b)
elif oper == "*":
    print(a*b)
elif oper=="/":
    print(a/b)
else:
    print("operador no aceptado")