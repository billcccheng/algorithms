#!/usr/bin/env python3
arr = [11, 10, 5, 7 ,8, 1, 3]
print('Original Array: ' + str(arr))

# QUICKSORT
def partition(a, low, high):
    pivot = a[high]
    i = low
    for j in range(low, high):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i+=1
    a[i], a[high] = a[high], a[i]
    return i

def quicksort(a, low, high):
    if low > high:
        return
    i = partition(a, low, high)
    quicksort(a, low, i-1)
    quicksort(a, i+1, high)

quicksort(arr, 0, len(arr)-1)
print('Sorted Array:   ' + str(arr))

