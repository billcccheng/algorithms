#!/usr/bin/env python3

arr = [11, 10, 5, 8, 7, 1, 3]
print('Original Array: ' + str(arr))

# SELECTION SORT
def selectionsort(a):
    for i in range(len(a)):
        min_i = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]

selectionsort(arr)
print('Sorted Array:   ' + str(arr))
