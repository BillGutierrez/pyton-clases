# esta_corriendo = False 
# esta_bloqueando = True
# esta_saltando = True

# if not esta_corriendo:
#     if not esta_bloqueando:
#         if not esta_saltando:
#             print("Drakarys")
#         else:
#             print("No puedo atacar mientras salto")
#     else:
#         print("No puedo atacar mientras bloqueo")
# else:
#     print("No puedo atacar mientras corro")

def mostrar_mensaje(esta_corriendo, esta_bloqueando, esta_saltando):
    if esta_corriendo:
        print("No puedo atacar mientras corro")
    elif esta_bloqueando:
        print("No puedo atacar mientras bloqueo")
    elif esta_saltando:
        print("No puedo atacar mientras salto")                            
    else:
        print("Drakarys")
          
mostrar_mensaje(True, False, False)
mostrar_mensaje(False, True, True)
mostrar_mensaje(False, False, True)