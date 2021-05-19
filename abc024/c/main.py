#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, D, K = map(int, input().split())
    L = [None] * D
    R = [None] * D
    for i in range(D):
        L[i], R[i] = map(int, input().split())
    S = [None] * K
    T = [None] * K
    for i in range(K):
        S[i], T[i] = map(int, input().split())

    ans = [0] * K
    now = S[:]
    for j in range(K):
        for i in range(D):
            if L[i] <= now[j] <= R[i]:
                ans[j] = i+1
                if now[j] < T[j]:
                    if T[j] <= R[i]:
                        now[j] = T[j]
                        ans[j] = i+1
                        break
                    else:
                        now[j] = R[i]
                else:
                    if T[j] >= L[i]:
                        now[j] = T[j]
                        ans[j] = i+1
                        break
                    else:
                        now[j] = L[i]
        # print(now)
    [print(a) for a in ans]
                


if __name__ == "__main__":
    main()
