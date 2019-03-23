#!/usr/local/bin/python3
import random
arr = list(range(10))
random.shuffle(arr)
print('Original Array: ' + str(arr))

# HEAPSORT
def heapify(a, n, i):
    max_i = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and a[max_i] < a[l]:
        max_i = l
    if r < n and a[max_i] < a[r]:
        max_i = r
    if max_i != i:
        a[max_i], a[i] = a[i], a[max_i]
        heapify(arr, n, max_i)

def heapsort(a):
    n = len(a)
    # Heapify first
    for i in range(n-1, -1, -1):
        heapify(a, n, i)
    # Root is max now. Swap root with last element...(i) and heapify root
    for i in range(n-1, -1, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

heapsort(arr)
print('Sorted Array:   ' + str(arr))
