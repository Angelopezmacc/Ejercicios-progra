
def Contador_de_Aa(cad):
    count = 0 
    for i in range(len(cad)):
        if (cad[i]=="a") or (cad[i]=="A") :
            count = count + 1
    return count


cad = input ("Escribe Caracteres: ")
v1=Contador_de_Aa(cad)
print(v1)



