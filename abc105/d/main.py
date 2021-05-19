#!/usr/bin/env python3
from itertools import accumulate
from collections import Counter


def main():
    N, M = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    modA = [a % M for a in accumulate(A)]
    # print(modA)
    ans = 0
    for l in Counter(modA).values():
        # print(l)
        ans += l * (l - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
