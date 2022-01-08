
import sys

def adding (list1, c):
    z=[]
    for i in list1:
        j=c+str(i)
        z.append(j)
    return z


def test(pasa):
    lnum=sys._getframe(1).f_lineno
    if pasa:
        msg = "prueba en la linea {0} ok".format(lnum)
    else:
        msg="prueba en la linea {0} fallo".format(lnum)
    print(msg)
    
def testSuite():
    test(adding([1,2,3,4], 'e') == ['e1', 'e2', 'e3', 'e4'])
    test(adding(['q','p','g'], 'A') == ['Aq', 'Ap', 'Ag'])
    test(adding([1,2.3,4.5], '-') == ['-1', '-2.3', '-4.5'])

testSuite()