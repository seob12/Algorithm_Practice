class ESM:
    
    def smBF(self,T, P): 
        m = len(P) 
        n = len(T) 
        for i in range(n-m+1): 
            j = 0
            while(j < m): 
                if (T[i + j] != P[j]): 
                    break
                j += 1
            if (j == m):  
                print("Pattern {} found at index {} ".format (T[i:i+m],i))
                
    def bcShift(self, P):
        NO_OF_CHARS = 128 
        m = len(P)                	
        tbl = [m]*NO_OF_CHARS       	
        for i in range(m-1):     		
            tbl[ord(P[i])] = m-1-i	
        return tbl
    
    def smHP(self, T, P): 
        m = len(P)                      
        n = len(T)                      
        tbl = self.bcShift(P)              
        i = m-1                         
        while(i <= n-1):                
            k = 0                       
            while k <= m-1 and P[m-1-k]==T[i-k]:    
                k += 1                  
            if k == m :
                print("Pattern {} found at index {} ".format (T[i-m+1:i+1],i-m+1)) 
                i +=1                
            else :                      
                i += tbl[ord(T[i])]       
                     

    def tblLPS(self, P):
        m=len(P)
        tbl = [0]
        for i in range(1, m):
            j = tbl[i - 1]
            print(P,' i=',i, ' j=',j,' LPS=',tbl)
            while j > 0 and P[j] != P[i]:
                j = tbl[j - 1]
            if P[j] == P[i]:
                tbl.append(j + 1)
            else:
                tbl.append(j)
        print(P,' i=',i, ' j=',j,' LPS=',tbl)
        return tbl
        
    def smKMP(self, T, P):
        n=len(T)
        m=len(P)
        tbl, j = self.tblLPS(P),  0
        for i in range(n):
            while j > 0 and T[i] != P[j]:
                j = tbl[j - 1]
                
            print(' i=',i, ', j=',j, ',  Pattern =',P, ', Text =', T)
            if T[i] == P[j]: j += 1
            if j == m: 
                print("Pattern {} found at index {} ".format (T[i-j+1:i-j+1+m],i-j+1)) 
                j = tbl[j - 1]

        print(' i=',i, ', j=',j, ',  Pattern =',P, ', Text =', T)