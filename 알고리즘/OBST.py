import random
import sys

class Node:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq
    def __repr__(self):
        return "Node({},{})".format(self.key, self.freq)

class OBST:
        
    def findMinCostRec(self, freq, i, j, level):
        if j < i:
            return 0
        minCost = sys.maxsize
        for k in range(i, j + 1):
            leftMinCost = self.findMinCostRec(freq, i, k - 1, level + 1)
            rightMinCost = self.findMinCostRec(freq, k + 1, j, level + 1)
            minCost = min(minCost, freq[k] * level + leftMinCost+ rightMinCost)
        return minCost
      
    def findMinCostDP(self,nodes):
            nodes.sort(key=lambda node: node.key)
            n = len(nodes)
 
            keys = [nodes[i].key for i in range(n)]
            freqs = [nodes[i].freq for i in range(n)]
            A = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
            sumF = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
            R = [[i if i == j else 0 for j in range(n)] for i in range(n)]
 
            for diagonal in range(2, n + 1):
                for i in range(n - diagonal + 1):
                    j = i + diagonal - 1
 
                    A[i][j] = sys.maxsize  # set the value to "infinity"
                    sumF[i][j] = sumF[i][j - 1] + freqs[j]
                    for k in range(R[i][j - 1], R[i + 1][j] + 1):  
                        left = A[i][k - 1] if k != i else 0  
                        right = A[k + 1][j] if k != j else 0  
                        cost = left + sumF[i][j] + right
 
                        if A[i][j] > cost:
                            A[i][j] = cost
                            R[i][j] = k
            return A,R
        
    def print_BST(self, root, key, i, j, parent, is_left):
        if i > j or i < 0 or j > len(root) - 1:
            return
 
        node = root[i][j]
        if parent == -1:  
            print(f"{key[node]} is the root of the binary search tree.")
        elif is_left:
            print(f"{key[node]} is the left child of key {parent}.")
        else:
            print(f"{key[node]} is the right child of key {parent}.")
 
        self.print_BST(root, key, i, node - 1, key[node], True)
        self.print_BST(root, key, node + 1, j, key[node], False)