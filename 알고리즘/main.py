from Lab01 import *

def testMul():
    Lab1 = Lab01()
    S= [[1 for col in range(3)] for row in range(3)]
    T = [[1 for col in range(3)] for row in range(3)]
    x=4
    Loc=Lab1.MatrixMul(x, S, T)
    if Loc!=-1:
        print('result is', Loc)
    else:
        print("Element not fount")


def hanoi():
    print('Lets go')
    #testSS()
    Lab1 = Lab01()
    n = 50
    #print('{}th fibonacci term is {} '.format(n, Lab1.fibonacciItr(n)))
    #print("{}th fibonacci term using recursive is = {} ".format(n, Lab1.fibonacciRec(n)))
    Lab1.hanoi(10,1,2,3)

if __name__ == '__main__':
    testMul()