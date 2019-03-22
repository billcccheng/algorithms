#!/usr/bin/env python3
from functools import reduce

def bitwise_or_range(m, n):
    if len(bin(m)) != len(bin(n)):
        left_shift = max(m.bit_length(), n.bit_length())
        return (1 << left_shift) - 1
    left_shift = 0
    while m != n:
        m >>= 1
        n >>= 1
        left_shift += 1
    return (n << left_shift) + ((1 << left_shift) - 1)

def main():
    a, b = 12, 18
    correct_res = reduce(lambda a, b: a | b, range(a, b+1))
    print(f'[{a}, {b}] bitwise or: {bitwise_or_range(a, b)}')
    # Testing Purpose
    print(bitwise_or_range(a, b) == correct_res)

if __name__ == '__main__':
    main()

