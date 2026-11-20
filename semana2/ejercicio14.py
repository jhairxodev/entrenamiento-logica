#CONTRASEÑA

contraseña = "Adm123"
contador = 0
intentos_max = 3 

while contador < intentos_max:
    intento= (input("Ingresa la contraseña: "))
    if intento == contraseña:
        print( "BIENVENIDO")
        break
    else:
        contador += 1
        print("CONTRASEÑA INCORRECTA")
if contador == intentos_max:
    print("USUARIO BLOQUEADO")    
    