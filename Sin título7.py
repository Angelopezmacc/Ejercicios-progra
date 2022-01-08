print ('Programa para calcular Fibonacci\n')
p=7
lmt=0
rep='   '
while p>0:
    while True:
        try:
            lmt=raw_input('Hasta cual numero desea hacer Fibonacci? \n ->')
            lmt=int(lmt)
            if lmt>0:
                break
            else:
                print ('Valor incorrecto. Digite un numero entero positivo.')
        except:
            print ('Valor incorrecto. Digite un numero entero positivo.'()
 
   
    b=1
    rsl= a+b
    flg=0
    print a
    print b
    a=b
    while rsl<=lmt:
        print rsl
        if flg==0:
            rsl=rsl+a
            a=rsl
            flg=1
        else:
            rsl=rsl+b
            b=rsl
            flg=0
 
    rep=raw_input('\nDesea repetir el programa?(si o no) \n ->')
    while rep !='si' and rep !='no':
        rep=raw_input('Respuesta invalida. Vuelva a intentarlo. \nDesea repetir el programa?(si o no)')
    if rep=='no':
        print ('\nGracias por usar nuestro programa!')
        break
    elif rep=='si':
        print ('\nReiniciando... \n\n')