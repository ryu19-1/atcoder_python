#!/usr/bin/env python3
from collections import deque

INF = 10**12


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    adj = [[] for _ in range(W*H)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    s = -1
    g = -1

    for i in range(H):
        for j in range(W):
            if S[i][j] == 's':
                s = W * i + j
            elif S[i][j] == 'g':
                g = W * i + j
            # for k in range(4):
            #     y = i + dy[k]
            #     x = j + dx[k]
            #     if 0 <= y < H and 0 <= x < W:
            #         if S[y][x] != '#':
            #             adj[W * i + j].append((W * y + x, 0))
            #         else:
            #             adj[W * i + j].append((W * y + x, 1))
    # print(adj)
    queue = deque([s])
    visit = [INF] * (H*W)
    visit[s] = 0

    while queue:
        now = queue.popleft()
        i = now // W
        j = now % W
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < H and 0 <= x < W:
                c = 1
                if S[y][x] != '#':
                    c = 0
                if visit[now]+c < visit[W*y+x]:
                    queue.append(W * y + x)
                    visit[W * y + x] = visit[now] + c
    # print(visit)
    if visit[g] <= 2:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
