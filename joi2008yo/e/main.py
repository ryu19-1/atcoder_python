#!/usr/bin/env python3
from heapq import heappop, heappush

def main():
    N, M, K, S = map(int, input().split())
    P, Q = map(int, input().split())
    C = [0] * N
    for _ in range(K):
        C[int(input())-1] = 1# ゾンビタウン

    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int(x)-1, input().split())
        print(a,b)
        # adj[a-1].append((b-1, ))
        # adj[b-1].append(a-1)

if __name__ == "__main__":
    main()
