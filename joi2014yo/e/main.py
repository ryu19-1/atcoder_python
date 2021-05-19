#!/usr/bin/env python3
from heapq import heappop, heappush
from collections import deque

def main():
    N, K = map(int, input().split())
    C = [None] * N
    R = [None] * N
    for i in range(N):
        C[i], R[i] = map(int, input().split())

    adj = [[] for _ in range(N)]
    for _ in range(K):
        a, b = map(lambda x: int(x)-1, input().split())
        adj[a].append(b)
        adj[b].append(a)

    INF = 10**12
    q = [0] # 始点のコストとindex
    d = [INF] * N
    d[0] = 0
    
    while len(q) > 0:
        u = heappop(q)
        
        queue = deque([u])
        visit = [-1] * N
        visit[u] = 0
        v_list = []# 町uからR[u]本以内の道路で着く町の集合
        
        while queue:
            now = queue.popleft()
            if visit[now] < R[u]:
                for v in adj[now]:
                    if visit[v] < 0:
                        v_list.append(v)
                        queue.append(v)
                        visit[v] = visit[now] + 1

        for w in v_list:
            tmp = d[u] + C[u]
            if tmp < d[w]:
                d[w] = tmp
                heappush(q, w)
    print(d[N-1])
    

if __name__ == "__main__":
    main()
