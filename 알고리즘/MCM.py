import sys
import random

class MCM:
    def getMatricesDim(self, n):
        dims=[]
        for i in range(n+1):
            dims.append(random.randint(1, 9))
        for i in range(n):
            print("M{}({} x {}) ".format(i+1,dims[i], dims[i+1] ))
        
        return dims
    
    def matrixChainMultiplicationRec(self, dims, i, j):
        if j <= i + 1:
            return 0
        minmul = sys.maxsize
 
        for k in range(i + 1, j):
            cost = self.matrixChainMultiplicationRec(dims, i, k)
            cost += self.matrixChainMultiplicationRec(dims, k, j)
            cost += dims[i] * dims[k] * dims[j]
 
            if cost < minmul:
                minmul = cost
        return minmul
    
    def matrixChainMultiplicationDP(self,dims):
        n = len(dims) - 1

        M = [[0 for x in range(0, n)] for y in range(0, n)]
        P = [[0 for x in range(0, n)] for y in range(0, n)]

        for i in range(0,n):
            P[i][i] = 0
        for l in range(2, n+1):
            for i in range(0, n - l + 1):
                j = i + l - 1 
                if i < j: 
                    cost = [M[i][k] + M[k+1][j] + dims[i] * dims[k+1] * dims[j+1] for k in range(i, j)]
                    (P[i][j], M[i][j]) = min(enumerate(cost), key=lambda x: x[1])
                    print (i, j, [k for k in enumerate(cost)])

                    P[i][j] = P[i][j] + i + 1 

        return M,P

    
    def printOrder(self,P, i, j):
        if i == j:
            print ("A_{}".format(i+1), end="")
        else:
            print ("(", end="")
            self.printOrder(P, i, P[i][j]-1)
            self.printOrder(P, P[i][j], j)
            print (")",end="")
            