tiempo = int(input("ingrese su tiempo de servicio: "))
salario = float(input("ingrese su salario: "))
if tiempo > 3:
    bonificacion = salario + (salario*5)/100
else:
    bonificacion=salario
    
print("su salario total es: ", bonificacion)