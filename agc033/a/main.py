#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    adj = [[] for _ in range(W*H)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    # 黒のマスからbfsする
    queue = deque()
    visit = [-1] * (W*H)

    for i in range(H):
        for j in range(W):
            if A[i][j] == '#':
                queue.append(W*i + j)
                visit[W*i + j] = 0
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < H and 0 <= x < W:
                    adj[W*i + j].append(W*y + x)
    
    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                visit[u] = visit[now] + 1
    print(max(visit))

if __name__ == "__main__":
    main()
