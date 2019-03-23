#!/usr/bin/env python3
import random
arr = list(range(10))
random.shuffle(arr)
print(arr)


def mergesort(subarray):
    if len(subarray) == 1:
        return subarray
    mid = len(subarray)//2
    L = mergesort(subarray[:mid])
    R = mergesort(subarray[mid:])
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            subarray[k] = L[i]
            i+=1
        else:
            subarray[k] = R[j]
            j+=1
        k+=1
    while i < len(L):
        subarray[k] = L[i]
        i+=1
        k+=1
    while j < len(R):
        subarray[k] = R[j]
        j+=1
        k+=1
    return subarray

mergesort(arr)
print(arr)

