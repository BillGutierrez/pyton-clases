edad1 = int(input("ingrese edad1: "))
edad2 = int(input("ingrese edad2: "))
edad3 = int(input("ingrese edad3: "))

if edad1>edad2 and edad1>edad3:
    print("el mayor tiene: ", edad1)
elif edad2>edad1 and edad2>edad3:
    print("el mayor tiene: ", edad2)
else:
    print("el mayor tiene: ", edad3)