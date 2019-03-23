#!/usr/bin/env python3

arr = [11, 10, 5, 8, 7, 1, 3]
print('Original Array: ' + str(arr))

#  INSERT SORT
def insertionsort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

insertionsort(arr)
print('Sorted Array:   ' + str(arr))

