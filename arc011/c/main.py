#!/usr/bin/env python3
import sys
from collections import deque, Counter
sys.setrecursionlimit(10**6)

def dfs(v):
    ans.append(s[v])
    # print(v,s[v],visit[v],adj[v])
    if v == 0:
        return
    for u in adj[v]:
        # print(u,s[u],visit[u])
        if visit[u] == visit[v]-1:
            dfs(u)
            break
    return

first, last = input().split()
if first == last:
    print(0)
    print(first)
    print(last)
    exit()

L = len(first)
N = int(input())
s = [first,last]
for i in range(N):
    s.append(input())

adj = [[] for _ in range(N+2)]
ans = []
queue = deque([0])
visit = [-1] * (N+2)
visit[0] = 1

for i in range(N+2):
    for j in range(i+1,N+2):
        diff = 0
        for k in range(L):
            if s[i][k] != s[j][k]:
                diff += 1
        if diff == 1:
            # if i != 1:
            #     adj[i].append(j)
            # if i != 0:
            #     adj[j].append(i)
            adj[i].append(j)
            adj[j].append(i)

while queue:
    now = queue.popleft()
    for u in adj[now]:
        if visit[u] < 0:
            queue.append(u)
            visit[u] = visit[now] + 1

# print(adj)

if visit[1] < 0:
    print(-1)
else:
    # dfsで終点から辿っていく
    print(visit[1]-2)
    dfs(1)
    for a in ans[::-1]:
        print(a)
    # print(visit)