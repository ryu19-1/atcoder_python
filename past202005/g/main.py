#!/usr/bin/env python3
from collections import deque

def main():
    N, X, Y = map(int, input().split())
    c = [list('.'*403) for _ in range(403)]
    # 障害物を設置する
    for i in range(N):
        a,b = map(int, input().split())
        c[b+201][a+201] = '#'# 障害物

    W = 403 # -201 -> 0
    H = 403
    adj = [[] for _ in range(W*H)]
    dx = [1,0,-1,1,-1,0 ]
    dy = [1,1, 1,0, 0,-1]
    
    for i in range(H):
        for j in range(W):
            if c[i][j] == '.':
                for k in range(6):
                    y = i + dy[k]
                    x = j + dx[k]
                    if 0 <= y < H and 0 <= x < W:
                        if c[y][x] == '.':
                            adj[W*i + j].append(W*y + x)

    
    queue = deque([201*W+201])
    visit = [-1] * (W*H)
    visit[201*W+201] = 0# (0,0)
    
    while queue:
        now = queue.popleft()
        # print(adj[now])
        for u in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                visit[u] = visit[now] + 1
    print(visit[(201+Y)*W+(201+X)])
    # print(X,Y)

if __name__ == "__main__":
    main()
