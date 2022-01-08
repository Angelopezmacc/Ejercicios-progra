def count(sub,cadena):
    n=0
    m=0
    counter=0
    for n in range(len(cadena)-1):
        x=cadena.find(sub,m)
        if x!=-1:
            counter+=1
            m=x+1
            
    return counter
    


import sys

def test(pasa):
    lnum=sys._getframe(1).f_lineno
    if pasa:
        msg = "prueba en la linea {0} ok".format(lnum)
    else:
        msg="prueba en la linea {0} fallo".format(lnum)
    print(msg)
    
def testSuite():
    test(count("is","missisipi") == 2)
    test(count("an","banana") == 2)
    test(count("ana","banana") == 2)
    test(count("nana","banana") == 1)
    test(count("nanan","banana") == 0)
    test(count("aaa","aaaaaa") == 4)

testSuite()