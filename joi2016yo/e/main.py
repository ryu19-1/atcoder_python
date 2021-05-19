#!/usr/bin/env python3
from heapq import heappop, heappush
from collections import deque

def main():
    N, M, K, S = map(int, input().split())
    P, Q = map(int, input().split())
    
    INF = 10**12
    X = set([int(input()) for _ in range(K)])

    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    # 危険な町を調べる
    C = [0] * N

    for x in X:
        # ゾンビタウンをbfsで求める
        queue = deque([x-1])
        C[x-1] = 1
        visit = [-1] * N
        visit[x-1] = 0
        
        while queue:
            now = queue.popleft()
            for u in adj[now]:
                if visit[u] < 0 and visit[now] < S:
                    C[u] = 1
                    queue.append(u)
                    visit[u] = visit[now] + 1

    # ゾンビタウンを通ってはいけないので封鎖する
    for x in X:
        adj[x-1] = []

    q = [0]# 始点
    d = [INF] * N
    d[0] = 0

    while len(q) > 0:
        u = heappop(q)
        for v in adj[u]:
            tmp = d[u] + [P,Q][C[v]]
            if tmp < d[v]:
                d[v] = tmp
                heappush(q, v)
    print(d[N-1]-[P,Q][C[N-1]])

if __name__ == "__main__":
    main()