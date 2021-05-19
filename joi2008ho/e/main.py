#!/usr/bin/env python3
from collections import deque


def main():
    H, W = map(int, input().split())
    N = int(input())
    x1 = [None] * N
    x2 = [None] * N
    y1 = [None] * N
    y2 = [None] * N
    x = set()
    x.add(0)
    x.add(W)
    y = set()
    y.add(0)
    y.add(H)
    for i in range(N):
        x1[i], y1[i], x2[i], y2[i] = map(int, input().split())
        x.add(x1[i])
        x.add(x2[i])
        y.add(y1[i])
        y.add(y2[i])

    x = sorted(x)
    y = sorted(y)
    check = [[1] * (len(x)-1) for _ in range(len(y)-1)]
    for i in range(len(y)-1):
        for j in range(len(x) - 1):
            for k in range(N):
                if x1[k] <= x[j] and x[j + 1] <= x2[k] and y1[k] <= y[i] and y[i + 1] <= y2[k]:
                    check[i][j] = 0
                    break

    print(x, y)
    W = len(x) - 1
    H = len(y) - 1
    adj = [[] for _ in range(W*H)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(H):
        for j in range(W):
            if check[i][j] == 0:
                continue
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < H and 0 <= x < W:
                    if check[y][x] == 1:
                        adj[W*i + j].append(W*y + x)

    ans = 0
    visit = [-1] * (H*W)
    for i in range(H*W):
        if visit[i] >= 0:
            continue
        queue = deque([i])
        visit[i] = ans

        while queue:
            now = queue.popleft()
            for u in adj[now]:
                if visit[u] < 0:
                    queue.append(u)
                    visit[u] = visit[now]

        ans += 1
        print(ans, visit)
    print(adj)


if __name__ == "__main__":
    main()
