#!/usr/bin/env python3
from heapq import heappop, heappush
INF = 10**12

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v, l = map(int, input().split())
        adj[u-1].append((l,v-1))
        adj[v-1].append((l,u-1))
    
    ans = INF
    # dijkstraで家1からの最短経路を計算
    for dist,i in adj[0]:
        q = [(0,0)]
        cost = [INF] * N
        cost[0] = 0
        
        while len(q) > 0:
            c, v = heappop(q)
            for d,u in adj[v]:
                if v == 0 and u == i:
                    continue
                tmp = cost[v] + d
                if tmp < cost[u]:
                    cost[u] = tmp
                    heappush(q,(tmp,u))
        res = dist + cost[i]
        if res < ans:
            ans = res
    print(ans) if ans < INF else print(-1)

if __name__ == "__main__":
    main()