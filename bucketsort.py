#!/usr/local/bin/python3
import random
import math
arr = [int(100*random.random()) for i in range(100)]
print(arr)

def bucket_sort(alist):
    largest = max(alist)
    smallest = min(alist)
    n = len(alist)
    size = math.ceil((largest - smallest)/n)
    buckets = [[] for _ in range(n//size)]
    for i in range(n):
        j = (alist[i] - smallest)//size
        if j != n:
            buckets[j].append(alist[i])
        else:
            buckets[-1].append(alist[i])
    print(buckets)
    buckets = [sorted(b) for b in buckets]
    return sum(buckets, [])

print(bucket_sort(arr))
