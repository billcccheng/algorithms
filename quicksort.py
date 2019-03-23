#!/usr/bin/env python3
import random
arr = list(range(20))
random.shuffle(arr)
print('Original Array: ' + str(arr))

# QUICKSORT
def partition(A, low, high):
    pivot = low
    for j in range(low, high):
        if A[j] <= A[high]:
            A[pivot], A[j] = A[j], A[pivot]
            pivot+=1
    A[pivot], A[high] = A[high], A[pivot]
    return pivot

def quicksort(a, low, high):
    if low > high:
        return
    i = partition(a, low, high)
    quicksort(a, low, i-1)
    quicksort(a, i+1, high)

quicksort(arr, 0, len(arr)-1)
print('Sorted Array:   ' + str(arr))

