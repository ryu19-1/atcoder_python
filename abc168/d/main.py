#!/usr/bin/env python3
from collections import deque

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    queue = deque([0])
    visit = [-1] * N
    visit[0] = 0# 部屋1の親はないので

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                visit[u] = now
    if -1 in visit:
        print('No')
    else:
        print('Yes')
        [print(v+1) for v in visit[1:]]

if __name__ == "__main__":
    main()
