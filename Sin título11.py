voc1 = "aeiouAEIOU"
voc=[]
for i in voc1:
    voc.append(i)
#print(voc)    

C = input("Ingrese una palabra")

def RemoveVocals(C):
    out=""
    for i in C:
        if i not in voc:
            out=out+i
    return(out)
       
a=RemoveVocals(C)
print(a)