
class Lab09:
    def binomialCoeffDP(self,n, k):
        B = [[0 for x in range(k + 1)] for x in range(n + 1)]
        for i in range(n + 1):
            for j in range(min(i, k) + 1):
                if j == 0 or j == i:
                    B[i][j] = 1
                else:
                    B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
                    print("(i,j) ({},{}) -> B[i][j]={} = B[i - 1][j - 1]={} + B[i - 1][j]={}".format(i, j, B[i][j], B[i - 1][j - 1], B[i - 1][j]))
        return B[n][k]


    def binomialCoeffRec(self, n, k):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return self.binomialCoeffRec(n - 1, k - 1) + self.binomialCoeffRec(n - 1, k)

    def numberOfPathsRec(self, m, n):
        if (m == 1 or n == 1):
            return 1
        return self.numberOfPathsRec(m - 1, n) + self.numberOfPathsRec(m, n - 1)

    def numberOfPathsDP(self, n, m):
        print("numberOfPaths by DP")
        B = [[0 for i in range(n)] for j in range(m)]

        for j in range(n):
            B[0][j] = 1
        for i in range(m):
            B[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                B[i][j] = B[i - 1][j] + B[i][j - 1]

        return B


    def numberOfPathsComb(self,m, n):
        print("numberOfPaths by using combinatorics")
        paths = 1
        for i in range(n, (m + n - 1)):
            paths *= i
            paths //= (i - n + 1)
            print("i={}, paths = {}".format(i, paths))

        return paths