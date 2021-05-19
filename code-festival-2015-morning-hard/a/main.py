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
    N = int(input())
    A = list(map(int, input().split()))
    d = deque(A)
    # print(d)
    ans = 0
    for i in range((N - 1) // 2):
        a = d[0] + (d[0] + d[1] + 1)
        b = d[-1] + (d[-1] + d[-2] + 1)
        if a <= b:
            ans += a
            a0 = d.popleft()
            a1 = d.popleft()
            d.appendleft(a0+a1+1)
            a0 = d.popleft()
            a1 = d.popleft()
            d.appendleft(a0+a1+1)
            # A = [A[0] + A[1] + 1] + A[2:]
            # A = [A[0] + A[1] + 1] + A[2:]
        else:
            ans += b
            a0 = d.pop()
            a1 = d.pop()
            d.append(a0+a1+1)
            a0 = d.pop()
            a1 = d.pop()
            d.append(a0+a1+1)
            # A = A[:-2] + [A[-1] + A[-2] + 1]
            # A = A[:-2] + [A[-1] + A[-2] + 1]
    print(ans)


if __name__ == "__main__":
    main()
