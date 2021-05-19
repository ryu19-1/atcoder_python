#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = 1
    minP = min(P[:K])
    maxP = max(P[:K])
    for i in range(N - K + 1):
        if P[i] == minP and P[i + K - 1] == maxP:
            pass
        else:
            ans += 1
        minP


if __name__ == "__main__":
    main()
