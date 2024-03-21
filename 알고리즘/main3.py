from Lab03 import *
import sys
import math

def testBC():
    lab03 = Lab03()
    print(lab03.binomialCoeffRec(15,5))
    print(lab03.binomialCoeffDP(15,5))

def testPowerSet():
    lab03 = Lab03()
    S1 = [1,2,3]
    L1 = lab03.powerSet(S1)
    print('Power Set = ', L1)

    S2 = ['A', 'B']
    L2 = lab03.PowerSet(S2)
    print('Power Set = ', L2)

def testClosestPair():
    lab03 = Lab03()
    pList = [(2,3), (12,30), (40, 50), (5,1), (12, 10), (4,4), (3,3)]
    cp = lab03.closest_pair(pList)
    print('closest pair [{}, {}] '.format(cp[0], cp[1]))
    print('Distance between closest pair =  {:.2f}   '.format(lab03.distance(cp[0], cp[1])))

def testSM():
    lab03 = Lab03()
    txt = 'AABAAABABCCACABAAAAAAAAABBBAAABAA'
    pat = 'AABA'
    lab03.SM(txt, pat)

def testIntersection():
    lab03 = Lab03()
    A = [1,3,4,5,7,9,11,13,15,17]
    B = [2,4,6,8,10,12,14,16]
    C = lab03.intersectionSet(A,B)
    print('Intersection Set = ', C)

def testLSZM():
    lab03 = Lab03()
    matrix = [
        [9,7,16,5],
        [1,-6,-7,-3],
        [1,8,7,-9],
        [7,-2,0,12]
    ]
    for r in matrix:
        print(r)
    Z = lab03.maxzeroSumSubmatrix(matrix)
    for r in Z:
        print(r)

def testSum2():
    lab03 = sumArray()
    print(lab03.maxsum2([3,-5,4,3,-6,4,8,-5,3,-7,2,1]))



if __name__ == '__main__':
    testSum2()