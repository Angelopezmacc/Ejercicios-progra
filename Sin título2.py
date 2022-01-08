'''Escriba una función para encontrar la lista, en una lista de listas, 
cuya suma de elementos es la más alta.
'''

import sys

def highest_list (list1):
    z=[]
    for (q,w,e) in list1:
        suma=q+w+e
        if 
            
    return z


def test(pasa):
    lnum=sys._getframe(1).f_lineno
    if pasa:
        msg = "prueba en la linea {0} ok".format(lnum)
    else:
        msg="prueba en la linea {0} fallo".format(lnum)
    print(msg)
    
def testSuite():

    test(highest_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]) == [10,11,12])

testSuite()
