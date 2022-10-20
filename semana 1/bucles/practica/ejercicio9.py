esta_corriendo = False 
esta_bloqueando = True
esta_saltando = True

if not esta_corriendo:
    if not esta_bloqueando:
        if not esta_saltando:
            print("Drakarys")
        else:
            print("No puedo atacar mientras salto")
    else:
        print("No puedo atacar mientras bloqueo")
else:
    print("No puedo atacar mientras corro")