import sys
import copy

class CoinsCollection:
    def ccDP(self, A):
        F = copy.deepcopy(A)

        for j in A:
            print(j)
        for r in range(1, len(A)):
            F[r][0]=F[r-1][0]+ A[r][0]

        for c in range(1, len(A[0])):
            F[0][c] = F[0][c - 1] + A[0][c]

        for r in range(1, len(A)):
            for c in range(1, len(A[0])):
                F[r][c] =  A[r][c]+ max(F[r - 1][c], F[r][c - 1])
        for r in F:
            print(r)
        return F

    def paths(self, F):
        m, n = len(F), len(F[0])
        print(m,n)
        B = [['-' for i in range(n)] for j in range(m)]
        for r in B:
            print(r)
        row = m - 1
        column = n - 1
        print(row, column)
        B[row][column] = '*'

        while row >= 1:

            if column != 0 and (F[row][column - 1] > F[row - 1][column]):  # leftward
                B[row][column - 1] = '*'
                column = column - 1
            else:
                B[row - 1][column] = '*'  # upward
                row = row - 1
        # the remaining cells path of the first row
        column = column - 1
        while column >= 0:
            B[0][column] = '*'
            column = column - 1

        for r in B:
            print(r)
