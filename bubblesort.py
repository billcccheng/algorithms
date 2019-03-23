#!/usr/bin/env python3

arr = [11, 10, 5, 7 ,8, 1, 3]
print('Original Array: ' + str(arr))

# BUBBLESORT
def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

bubblesort(arr)
print('Sorted Array:   ' + str(arr))


