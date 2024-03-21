from Lab04 import *

def testHeapSort():
    lab04 = Lab04()
    A = random.sample(range(1, 30), 15)
    S = [0] * len(A)
    B = copy.deepcopy(A)
    print("Original  : ", A)
    lab04.heapsort(A)
    print("Heap Sort Result : ", A)

def testQuickSort():
    lab04 = Lab04()
    A = random.sample(range(1, 30), 15)
    S = [0] * len(A)
    B = copy.deepcopy(A)
    print("Original  : ", A)
    lab04.quicksort(A, 0, len(A) - 1)
    print("Quick Sort Result : ", A)

def testMergeSort():
    lab04 = Lab04()
    A = random.sample(range(1, 30), 15)
    S = [0] * len(A)
    B = copy.deepcopy(A)
    print("Original  : ", A)
    lab04.merge_sort_itr(A)
    # lab05.merge_sort(A, S, 0, len(A)-1)
    print("MergeSort Result : ", A)


def testCountingSort():
    lab04 = Lab04()
    A = random.sample(range(1, 30), 15)
    S = [0] * len(A)
    B = copy.deepcopy(A)
    print("Original  : ", A)
    k = max(A) + 1
    lab04.countingSort(A, k)
    print("Counting Sort Result : ", A)

def testradixSort():
    lab04 = Lab04()
    A = random.sample(range(1,30), 15)
    print('Original   :  ', A)
    lab04.radixSort(A)
    print('radix Sort Result : ', A)

def testmergemodify():
    lab04 = Lab04()
    A = random.sample(range(1, 30), 18)
    S = [0] * len(A)
    B = copy.deepcopy(A)
    print('Original   :  ', A)
    lab04.merge_sortmod(A)
    print('merge Sort Result : ', A)

def testcountinver():
    lab04 = Lab04()
    A = random.sample(range(1, 30), 15)
    S = [0] * len(A)
    B = copy.deepcopy(A)
    print('Original   :  ', A)
    lab04.count_inversions(A)
    print('count_inverse Sort Result : ', A)




def main():
    #testMergeSort()
    #testQuickSort()
    #testCountingSort()
    #testHeapSort()
    #testradixSort()
    testmergemodify()
    #testcountinver()
    


if __name__ == '__main__':
    main()