#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    s, g = map(lambda x: int(x)-1, input().split())
    M = int(input())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x-1].append(y-1)
        adj[y-1].append(x-1)

    # 頂点aからの最短経路を求める(道路の距離=1なのでBFSが素直な実装)
    queue = deque([s])
    visit = [-1] * N
    visit[s] = 0
    
    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                visit[u] = visit[now] + 1

    # 全ての道路に対して、結んでいる頂点の最短距離の差が1でなければDAGにはいらない
    for i in range(N):
        for j in range(N):
            if j in adj[i] and visit[j] - visit[i] != 1:
                adj[i].remove(j)

    # DAGが出来たのでDPで経路の総数を計算
    dp = [0]*N
    dp[s] = 1
    dpqueue = deque([s])
    m = 10**9+7
    
    while queue:
        now = dpqueue.popleft()
        for u in adj[now]:
            dpqueue.append(u)
            dp[u] += dp[now]
            dp[u] %= m
    
    print(dp[g])

if __name__ == "__main__":
    main()
