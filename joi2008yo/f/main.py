#!/usr/bin/env python3
from heapq import heappop, heappush


def main():
    n, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    INF = 10**12

    for _ in range(k):
        S = list(map(int, input().split()))
        if S[0] == 0:
            # Dijkstra
            q = [(0,S[1]-1)]# 始点
            d = [INF] * n
            d[S[1]-1] = 0

            while len(q) > 0:
                _, u = heappop(q)
                for v, cost in adj[u]:
                    tmp = d[u] + cost
                    if tmp < d[v]:
                        d[v] = tmp
                        heappush(q, (d[v], v))
            if d[S[2]-1] == INF:
                print(-1)
            else:
                print(d[S[2]-1])
        else:
            adj[S[1] - 1].append((S[2] - 1, S[3]))
            adj[S[2] - 1].append((S[1] - 1, S[3]))


if __name__ == "__main__":
    main()
