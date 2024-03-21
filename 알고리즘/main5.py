from Lab05 import *

def rankSelectionTest():
    lab05=Lab05()
    A = random.sample(range(1, 50), 30)
    print(A)
    medi=int(round((1+len(A))/2))
    largest= len(A)
    smallest=1
    print("element at rank {} is {} ".format(smallest, lab05.rankSelection(A, 0, len(A)-1, smallest)))
    print("element at rank {} is {} ".format(largest, lab05.rankSelection(A, 0, len(A) - 1, largest)))
    print("element at rank {} is {} ".format(medi, lab05.rankSelection(A, 0, len(A) - 1, medi)))
    A.sort()
    print(A)

def ternarySearchTest():
    lab05 = Lab05()
    A = random.sample(range(1, 50), 30)
    A.sort()
    print(A)
    key = 19
    p = lab05.ternarySearchRec(0, len(A) - 1, key, A)
    print("ternarySearchRec: Index of", key, "is", p)
    p = lab05.ternarySearchItr(A, key)
    print("ternarySearchItr: Index of", key, "is", p)
    #p = lab05.interpolationSearchRec(0, len(A) - 1, key, A)
    #print("interpolationSearchRec: Index of", key, "is", p)
    #p = lab05.interpolationSearchItr(A, key)
    #print("interpolationSearchItr: Index of", key, "is", p)

def findSLTest():
    lab05 = Lab05()
    A = random.sample(range(1,50), 30)
    A.sort()
    print(A)
    print('find Smallest result is: ', lab05.findSL(A))

def findSLPKTest():
    lab05 = Lab05()
    A = random.sample(range(1,50), 30)
    A.sort()
    print(A)
    print('findSLPK result is ', lab05.findSLPK(A))
    

def minMaxTest():
    lab05 = Lab05()
    A = random.sample(range(1, 3000), 15)
    print(A)
    minmax = lab05.getMinMax1(A)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)


def fackCoinTest():
    fc = FakeCoin(20)
    print("Fake Coin with weight:", fc.fake_coin_DQ2())


def POLTest():
    lab05 = Lab05()
    P = [(1, 1), (3, 5), (4, 6), (6, 6), (2, 3), (3, 5), (7, 3), (12, 3), (4, 14)]
    lab05.postOfficeLocation(P)

def bitflipstest():
    bf=BitFlips()
    res = bf.minBitFlips(3, 11193)
    print("No. of flips :",res)

def main():
    bitflipstest()
    #rankSelectionTest()
    #minMaxTest()
    #ternarySearchTest()
    #POLTest()
    #fackCoinTest()
    #findSLTest()
    #findSLPKTest()

if __name__ == '__main__':
    main()