numero = int(input("Ingresa un numero: "))
while numero !=1:
    if numero % 2 ==0:
        print(numero)
        numero=int(numero/2)
    else:
        print(numero)
        numero=int((numero*3)+1)
    if numero ==1:
        print("1")        
