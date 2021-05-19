#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    l = Counter(a)
    count = [0] * N
    count[0] = l[0]
    for i in range(1, N):
        if i not in l:
            continue
        count[i] = min(count[i-1], l[i])
    # print(count)
    ans = 0
    remind = K
    for i in range(N):
        ans += max(remind - count[i], 0)*i
        remind = min(remind, count[i])
    ans += remind * N
    print(ans)


if __name__ == "__main__":
    main()
