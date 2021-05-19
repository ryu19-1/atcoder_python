#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate, combinations

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [None] * M
    C = [None] * M
    I = [None for _ in range(M)]
    for i in range(M):
        B[i], C[i], *I[i] = map(lambda x: int(x)-1, input().split())
        B[i] += 1
        C[i] += 1

    ans = 0
    # 全探索するだけ
    for v in combinations(range(N),9):
        tmp = 0
        for u in v:
            tmp += A[u]
        for i in range(M):
            count = 0
            for j in range(C[i]):
                if I[i][j] in v:
                    count += 1
            if count >= 3:
                tmp += B[i]
        ans = max(ans,tmp)
    print(ans)

if __name__ == "__main__":
    main()
