#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

def main():
    H, W = map(int, input().split())
    Ch, Cw = map(lambda x: int(x)-1, input().split())
    Dh, Dw = map(lambda x: int(x)-1, input().split())
    S = [input() for _ in range(H)]

    adj = [[] for _ in range(W*H)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#': continue
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < H and 0 <= x < W:
                    if S[y][x] == '.':
                        adj[W*i + j].append(W*y + x)

    # ワープ可能な場所もadjに加える
    worp = [[] for _ in range(W*H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#': continue
            for kx in [-2,-1,0,1,2]:
                for ky in [-2,-1,0,1,2]:
                    if kx == ky == 0: continue
                    y = i + ky
                    x = j + kx
                    if W*y + x in adj[W*i + j]: continue
                    if 0 <= y < H and 0 <= x < W:
                        if S[y][x] == '.':
                            worp[W*i + j].append(W*y + x)
    
    start = W*Ch + Cw
    goal = W*Dh + Dw
    queue = deque([start])
    visit = [-1] * (W*H)
    visit[start] = 0
    
    while queue:
        nextq = queue.copy()
        while queue:
            now = queue.popleft()
            for u in adj[now]:
                if visit[u] < 0:
                    queue.append(u)
                    nextq.append(u)
                    visit[u] = visit[now]
        # print(nextq)
        while nextq:
            now = nextq.popleft()
            for u in worp[now]:
                if visit[u] < 0:
                    queue.append(u)
                    visit[u] = visit[now]+1
    
    print(visit[goal])

if __name__ == "__main__":
    main()
