#!/usr/bin/env python3
from heapq import heappop, heappush


def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    S = input()

    # N: A, N+1: B, N+2:C, N+3: D, N+4: E, N+5: F
    adj = [[] for _ in range(N + 6)]
    adj[N].append((X[0], N+4))
    adj[N].append((X[1], N+5))
    adj[N+1].append((X[0], N+3))
    adj[N+1].append((X[2], N+5))
    adj[N+2].append((X[1], N+3))
    adj[N+2].append((X[2], N+4))
    for i in range(N):
        t = 'ABC'.index(S[i])
        adj[i].append((0, N+t))
        adj[N+3+t].append((0, i))

    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append((c, b))
        adj[b].append((c, a))

    INF = 10**18
    q = [(0, 0)]  # 始点のコストとindex
    d = [INF] * (N+6)
    d[0] = 0

    while len(q) > 0:
        cost, u = heappop(q)
        if d[u] < cost:  # これ大事
            continue
        for c, v in adj[u]:
            tmp = d[u] + c
            if tmp < d[v]:
                d[v] = tmp
                heappush(q, (d[v], v))
    print(d[N-1])


if __name__ == "__main__":
    main()
