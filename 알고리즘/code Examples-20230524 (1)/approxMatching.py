class ApproximateMatching:
    def editDistanceDC(self,x, y):
        if len(x) == 0:
            return len(y)
        elif len(y) == 0:
            return len(x)
        else:
            distHor = self.editDistanceDC(x[:-1], y) + 1
            distVer = self.editDistanceDC(x, y[:-1]) + 1
            if x[-1] == y[-1]:
                distDiag = self.editDistanceDC(x[:-1], y[:-1])
            else:
                distDiag = self.editDistanceDC(x[:-1], y[:-1]) + 1
        return min(distHor, distVer, distDiag)
    
    def editDistanceDP(self,x, y):
        
        D = []
        for i in range(len(x)+1):
            D.append([0]*(len(y)+1))
        
        for i in range(len(x)+1):
            D[i][0] = i
        for i in range(len(y)+1):
            D[0][i] = i
        
        for i in range(1, len(x)+1):
            for j in range(1, len(y)+1):
                distHor = D[i][j-1] + 1
                distVer = D[i-1][j] + 1
                if x[i-1] == y[j-1]:
                    distDiag = D[i-1][j-1]
                else:
                    distDiag = D[i-1][j-1] + 1
                D[i][j] = min(distHor, distVer, distDiag)
        
        return D[-1][-1]