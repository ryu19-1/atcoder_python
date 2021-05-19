#!/usr/bin/env python3
from collections import Counter


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        a = list(map(int, input().split()))
        xor = 0
        for i in range(N):
            xor ^= a[i]
        if N % 2 == 0:  # コインをおく時に手番が変わらない
            for k, v in Counter(a).items():
                if v % 2 == 1:
                    print('First')
                    break
            else:
                print('Second')
        else:
            print('Second')


if __name__ == "__main__":
    main()
