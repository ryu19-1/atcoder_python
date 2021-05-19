#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(lambda x: int(x)-1, input().split())
        adj[A].append(B)
        adj[B].append(A)
    
    for i in range(N):
        ans = 0
        queue = deque([i])
        visit = [-1] * N
        visit[i] = 0
        
        while queue:
            now = queue.popleft()
            for u in adj[now]:
                if visit[u] < 0:
                    queue.append(u)
                    visit[u] = visit[now] + 1
                    if visit[u] == 2:
                        ans += 1
        print(ans)
    

if __name__ == "__main__":
    main()
