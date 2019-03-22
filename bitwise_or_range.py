#!/usr/bin/env python3
from functools import reduce

def bitwise_or_range(m, n):
    if len(bin(m)) != len(bin(n)):
        i = max(m.bit_length(), n.bit_length())
        return (1 << i) - 1
    i = 0
    while m != n:
        m >>= 1
        n >>= 1
        i+=1
    return (n << i) + ((1<<i) - 1)

def main():
    a, b = 7, 21
    print(f'[{a}, {b}] bitwise = {reduce(lambda a, b: a | b, range(a, b+1))}')
    # Testing Purpose
    print(bitwise_or_range(a, b) == reduce(lambda a, b: a | b, range(a, b+1)))

if __name__ == '__main__':
    main()

