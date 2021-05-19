#!/usr/bin/env python3
from heapq import heappop, heappush

def dijkstra(mid):
    adj = [[] for _ in range(W*H)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    start = -1
    goal = -1
    
    for i in range(H):
        for j in range(W):
            if s[i][j] == 'S':
                start = W*i+j
            elif s[i][j] == 'G':
                goal = W*i+j
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < H and 0 <= x < W:
                    if s[y][x] == '#':
                        adj[W*i+j].append((mid,W*y+x))
                    else:
                        adj[W*i+j].append((1,W*y+x))

    INF = 10**12
    q = [(0,start)] # 始点のコストとindex
    cost = [INF] * (H*W)
    cost[start] = 0
    
    while len(q) > 0:
        c, u = heappop(q)
        for d,v in adj[u]:
            tmp = cost[u] + d
            if tmp < cost[v]:
                cost[v] = tmp
                heappush(q, (tmp, v))
    
    return cost[goal]

# INPUT
H, W, T = map(int, input().split())
s = [input() for _ in range(H)]

# 答えxの値で二分探索
ok = 0
ng = 10**9
while ng - ok > 1:
    mid = (ok + ng)//2
    res = dijkstra(mid)
    if res <= T:
        ok = mid
    else:
        ng = mid

print(ok)