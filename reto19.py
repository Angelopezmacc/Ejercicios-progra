
x1 = (10002, 99550, [56,43,12],["China"], ["Quibdo", "Pasto", "Popayan", "Leticia"])    
x2=(1003,99987,[76,98,23],["Rusia"],["pereira","pasto","bogota","cali"])
x3=(109004,876909,[87,90,67],["Chile"],["barranquilla","medellin","cali","bogota"])
x4=(193990,83850,[43,765,43],["Colombia"],["cartagena","bogota","popayan","cali"])

productos=(x1,x2,x3,x4)


def PaisProcedencia(C):
    count1=0
    for (iden, pr, v, p, c) in productos:
        for i in p:            
            if i==C:
                count1+=1
    print(count1,"Productos provienen de ",C)
def VolumenMaximo(V):
    count2=0
    for (iden, pr, v, p, c) in productos:
        for i in v:
                vol=v[0]*v[1]*v[2]
                break
                return vol
        if vol <= V:
            
                count2+=1
            
    print(count2, "Productos tienen un volumen menor a ",V)
    
def Ciudad(y):
   count3=0
   for (iden, pr, v, p, c) in productos:
       for i in c:
           if i==y:
              count3+=1
   print(count3," productos se encuentran a la venta en la ciudad de ",y)
   
PaisProcedencia("China")
Ciudad("cali")
VolumenMaximo(265990000)

