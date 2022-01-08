def count_divisible(n): #se define la función
    count=0#crea un contador
    while n>0:# crea un ciclo while para que la función siga pidiendole números al usuario 
        num=int(input("Ingrese un numero entero: "))
        if num%n==0 and num!=0 and num>0:#va contando los numeros que son divisibles entre n y que son mayores a 0
            count+=1# se aumenta el contador cada vez que la condición se cumple
        if num<=0:# se da la condición en la cual el while se rompe
            break#se rompe el ciclo while
    return(count)
        
        
        

n = 3
cant = count_divisible(n)
print("Hubo {0} enteros positivos divisibles entre {1}".format(cant,n))

