import sys

class Lab02:
    def Power(self, x, n):
        if n == 0:
            return 1
        if n & 1:
            return x * self.power(x,n // 2) * self.power(x, (n//2))
        return self.power(x, n // 2) * self.power(x, (n//2))
    
    def Power2(self, n):
        if n == 0:
            return 1
        if n & 1:
            return 2 * self.Power2(n//2) * self.Power2(n//2)
        return self.Power2(n // 2) * self.Power2(n//2)
    
    def GE(self, A):
        n = len(A)
        for i in range(n-1):
            for j in range(i+1, n):
                ratio = A[j][i]/A[i][i]
                for k in range(n+1):
                    A[j][k] = A[j][k] - A[i][k] * ratio
        print(A)

    def ways(self, n):
        if n <= 2:
            return n
        else:
            return self.ways(n-1) * self.ways(n-2)
        
    def UE(self, A):
        n = len(A)
        for i in range(n-1):
            for j in range(i+1, n):
                if A[i] == A[j]:
                    return False
        return True
    
    def gcd(self, a, b):
        print('gcd', (a,b))
       
        if(b == 0):
            return a
        else:
            return self.gcd(b, a%b)

        