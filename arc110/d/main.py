#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
p = 10**9 + 7


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    if M < S:
        print(0)
        exit()
    # 答えは(M+N)C(S+N)=(M+N)C(M-S)
    ans = 1
    div = 1
    for i in range(N+S):
        ans *= M + N - i
        div *= N + S - i
        ans %= p
        div %= p
        # print(ans, div)
    print(ans*pow(div, p-2, p) % p)


if __name__ == "__main__":
    main()
