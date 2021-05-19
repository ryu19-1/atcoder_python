#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    N = int(input())
    S = input()
    B = 0
    W = S.count('.')
    ans = B+W
    for i in range(N):
        if S[i] == '#':
            B += 1
        else:
            W -= 1
        ans = min(ans, B+W)
    print(ans)

if __name__ == "__main__":
    main()
