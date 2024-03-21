from random import randint
import random
import copy

class Lab04:

    def merge_sort(self, A, S, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(A, S, left, mid)
            self.merge_sort(A, S, mid + 1, right)
            self.merge(A, S, left, mid, right)
    
    def merge(self, A, S,left, mid, right) :
        k = left					
        i = left					
        j = mid + 1				
        while i<=mid and j<=right :
            if A[i] <= A[j] :		
                S[k] = A[i]
                i, k = i+1, k+1
            else:
                S[k] = A[j]
                j, k = j+1, k+1

        if i > mid :				
            S[k:k+right-j+1] = A[j:right+1]	
        else :
            S[k:k+mid-i+1] = A[i:mid+1]		

        A[left:right+1] = S[left:right+1]		

    def merge_sort_itr(self,A):
 
        low = 0
        high = len(A) - 1
        S=[0] * len(A)
        m = 1
        while m <= high - low:
 
            for i in range(low, high, 2*m):
                left = i
                mid = i + m - 1
                right = min(i + 2*m - 1, high)
                self.merge(A, S, left, mid, right)
            m = 2*m


    def quicksort(self, A, low, high):
        if len(A)==1:
            return
        if low < high:
            pp = self.partition(A, low, high)  #pi Pivot position
            self.quicksort(A, low, pp - 1)
            self.quicksort(A, pp + 1, high)


    def partition(self,A, low, high):
        pivot = A[low]
        j=low
        for i in range(low+1,high+1):
            if (A[i] < pivot):
                j+=1
                A[j],A[i]=A[i],A[j]
        A[j],A[low]=A[low],A[j]   
        return j  
    
    def countingSort(self,A,k):
        size = len(A)
        B = [0] * size
        C = [0] * k

        for i in range(0, size):
            C[A[i]] += 1
        for i in range(1, k):
            C[i] += C[i - 1]
        
        i = size - 1
        while i >= 0:
            B[C[A[i]] - 1] = A[i]
            C[A[i]] -= 1
            i -= 1
        for i in range(0, size):
            A[i] = B[i]
            
            
    def placeSort(self,A, place):
        size = len(A)
        output = [0] * size
        count = [0] * 10

        for i in range(0, size):
            index = A[i] // place
            count[index % 10] += 1
    
        for i in range(1, 10):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            index = A[i] // place
            output[count[index % 10] - 1] = A[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            A[i] = output[i]


    def radixSort(self,A):
        max_element = max(A)
        print('max element : ', max_element)
        place = 1
        while max_element // place > 0:
            self.placeSort(A, place)
            place *= 10
    
   
    def insertionSort(self,A):
        for i in range(1, len(A)):
            value = A[i]
            j = i
        while j > 0 and A[j - 1] > value:
            A[j] = A[j - 1]
            j = j - 1
        A[j] = value
    
    def bubbleSort(self, A):
        for k in range(len(A) - 1):
            for i in range(len(A) - 1 - k):
                if A[i] > A[i + 1]:
                    swap(A, i, i+1)
    
             
    def swap(self, A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
    
    def heapify(self,A, n, i):
    
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
  
        if left < n and A[i] < A[left]:
            largest = left
  
        if right < n and A[largest] < A[right]:
            largest = right
  
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.heapify(A, n, largest)
            
    def buildheap(self, A):
        n = len(A)
        for i in range(n//2, -1, -1):
            self.heapify(A, n, i)
        return A        
        
    def heapsort(self, A):
        n = len(A)
        A=self.buildheap(A)
        for i in range(n-1, 0, -1):
            A[i], A[0] = A[0], A[i]
            self.heapify(A, i, 0)

    def inversionCount(self, A, S, left, right):
        if left == right:
            return 0
        else:
            mid = (left + right) // 2
            count = 0
            count += self.inversionCount(A, S, left, mid)
            count += self.inversionCount(A, S, mid + 1, right)
            count += self.mergeInversion(A, S, left, mid, right)

    def mergeInversion(self, A, aux, low, mid, high):
        k = i = low
        j = mid + 1
        count = 0
        while i <= mid and j <= high:
            if A[i] <= A[j]:
                aux[k] = A[i]
                i = i + 1
            else:
                aux[k] = A[j]
                j = j + 1
                count += (mid - i + 1)

            k = k + 1

        while i < mid:
            aux[k] = A[i]
            k = k + 1
            i = i + 1

        for i in range(low, high + 1):
            A[i] = aux[i]

        return count
    
    def merge_sortmod(self, arr):
        if len(arr) <= 1:
            return arr
    
        n = len(arr)
        mid1 = n // 3
        mid2 = 2 * n // 3
        left = self.merge_sortmod(arr[:mid1])
        middle = self.merge_sortmod(arr[mid1:mid2])
        right = self.merge_sortmod(arr[mid2:])
    
        i = j = k = 0
        while i < len(left) and j < len(middle) and k < len(right):
            if left[i] < middle[j]:
                if left[i] < right[k]:
                    arr[i+j+k] = left[i]
                    i += 1
                else:
                    arr[i+j+k] = right[k]
                    k += 1
            else:
                if middle[j] < right[k]:
                    arr[i+j+k] = middle[j]
                    j += 1
                else:
                    arr[i+j+k] = right[k]
                    k += 1
    
        while i < len(left) and j < len(middle):
            if left[i] < middle[j]:
                arr[i+j+k] = left[i]
                i += 1
            else:
                arr[i+j+k] = middle[j]
                j += 1
    
        while i < len(left) and k < len(right):
            if left[i] < right[k]:
                arr[i+j+k] = left[i]
                i += 1
            else:
                arr[i+j+k] = right[k]
                k += 1
    
        while j < len(middle) and k < len(right):
            if middle[j] < right[k]:
                arr[i+j+k] = middle[j]
                j += 1
            else:
                arr[i+j+k] = right[k]
                k += 1
    
        while i < len(left):
            arr[i+j+k] = left[i]
            i += 1
    
        while j < len(middle):
            arr[i+j+k] = middle[j]
            j += 1
    
        while k < len(right):
            arr[i+j+k] = right[k]
            k += 1
    
        return arr


    def count_inversions(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
    
    # Divide the array into two halves
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
    
    # Recursively count the inversions in the left and right halves
        count = self.count_inversions(left) + self.count_inversions(right)
    
    # Merge the sorted left and right halves, while counting the inversions
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[i+j+k] = left[i]
                i += 1
            else:
                arr[i+j+k] = right[j]
                j += 1
                count += len(left) - i
    
        while i < len(left):
            arr[i+j+k] = left[i]
            i += 1

        while j < len(right):
            arr[i+j+k] = right[j]
            j += 1
    
        return count