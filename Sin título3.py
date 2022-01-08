l1=float(input("Ingrese el valor del primer lado del triángulo: "))
l2=float(input("Ingrese el valor del segundo lado del triángulo: "))
l3=float(input("Ingrese el valor del tercer lado del triángulo: "))

if l1==l2==l3:
    print("Es un triángulo equilátero.")

elif (((l1==l2)and(l1 and l2 !=l3)) or ((l2==l3)and(l2 and l3 !=l1)) or ((l1==l3)and(l1 and l3 != l2))):
    print("El triángulo es isóceles.")
else:
    print("El triángulo es escaleno")