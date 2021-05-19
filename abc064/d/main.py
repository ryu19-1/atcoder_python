#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

def main():
    N = int(input())
    T = input()
    S = []
    for s in T:
        if s == '(':
            S.append(1)
        else:
            S.append(-1)
    S = list(accumulate(S))
    # print(S)
    minS = min(S)
    if minS < 0:
        for i in range(N):
            S[i] -= minS
    print('('*max(0,-minS) + T + ')'*S[-1])

if __name__ == "__main__":
    main()
