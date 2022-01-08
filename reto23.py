import sys

def test(pasa):
    lnum=sys._getframe(1).f_lineno
    if pasa:
        msg = "prueba en la linea {0} ok".format(lnum)
    else:
        msg="prueba en la linea {0} fallo".format(lnum)
    print(msg)


def remove_dups(lista):
    listanueva=[]    
    for i in lista:
        if i not in listanueva:
            listanueva.append(i)
            
    return listanueva


def testSuite():
    test(remove_dups([1, 2, 3, 4, 2, 4, 3, 1, 0]) == [1, 2, 3, 4, 0])
    test(remove_dups([6, 6, 8, 1, 3, 4, 3, 1, 1]) == [6, 8, 1, 3, 4])
    test(remove_dups([5, 2, 1, 1, 4, 5, 6]) == [5, 2, 1, 4, 6])
    test(remove_dups([6, 5, 4, 4, 2, 2, 1, 0]) == [6, 5, 4, 2, 1, 0])

testSuite()

