#!/usr/bin/env python3
from itertools import permutations


def main():
    N = int(input())
    S = input()
    for t in permutations(S, N):
        T = ''.join(t)
        if T == S or T[::-1] == S:
            continue
        print(T)
        exit()
    print('None')


if __name__ == "__main__":
    main()
