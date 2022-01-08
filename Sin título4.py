n1=float(input("Ingrese el primer número: "))
n2=float(input("Ingrese el segundo número: "))
n3=float(input("Ingrese el tecer número: "))

if n1<n2<n3:
    print(n1,n2,n3)
    
elif n2<n1<n3:
    print(n2,n1,n3)
elif n3<n2<n1:
    print(n3,n2,n1)
elif n1<n3<n2:
    print(n1,n3,n2)
elif n2<n3<n1:
    print(n2,n3,n1)
elif n3<n1<n2:
    print(n3,n1,n2)
else:
    print("Los números ingresados son iguales")    
