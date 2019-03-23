#!/usr/bin/env python3
import collections
import heapq

class Node:
    def __init__(self, weight, keys):
        self.keys = keys
        self.weight = weight
    def __lt__(self, other):
        return self.weight <= other.weight

def encode(frequency):
    heap = []
    for k, wt in frequency.items():
        heapq.heappush(heap, Node(wt, [[k, '']]))
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        lo_key = [[key, encoding + '0'] for key, encoding in lo.keys]
        hi_key = [[key, encoding + '1'] for key, encoding in hi.keys]
        new_node = Node(lo.weight + hi.weight, lo_key + hi_key)
        heapq.heappush(heap, new_node)
    return sorted(heap[0].keys, key=lambda x: (len(x[-1]), x))

def main():
    s = 'Count the number of times every character occurs. Use these counts to create an initial forest of one-node trees'
    frequency = collections.Counter(s)

    huff = encode(frequency)
    print("Symbol\tWeight\tHuffman Code")
    for c, v in huff:
        print("%s\t%s\t%s" % (c, frequency[c], v))

if __name__ == '__main__':
    main()

