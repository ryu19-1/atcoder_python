#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right, bisect_left
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N, K, C = map(int, input().split())
    S = input()
    countL = [0] * (N + 1)
    ansL = []
    nowork = 0
    for i in range(N):
        countL[i+1] = countL[i]
        if S[i] == 'o' and nowork == 0:
            countL[i + 1] += 1
            nowork = C
            ansL.append(i)
        else:
            nowork = max(0, nowork - 1)
    # print(ansL)

    countR = [0] * (N+1)
    nowork = 0
    ansR = []
    for i in range(N-1, -1, -1):
        countR[i] = countR[i+1]
        if S[i] == 'o' and nowork == 0:
            countR[i] += 1
            nowork = C
            ansR.append(i)
        else:
            nowork = max(0, nowork - 1)
    ansR.sort()
    # print(ansR)
    if len(ansL) > K:
        print()
    else:
        for i in range(len(ansL)):
            if ansL[i] == ansR[i]:
                print(ansL[i]+1)


if __name__ == "__main__":
    main()
