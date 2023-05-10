def solicitaUnNum (numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False
    
numero = input("escribe un numero: ") 
if solicitaUnNum(numero):
    print("ha introducido un numero valido")
else:
    print("el numero introducido no es valido")
           