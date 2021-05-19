#!/usr/bin/env python3
from collections import deque


def main():
    W, H, N = map(int, input().split())
    # XY = [list(map(lambda x: int(x)-1, input().split())) for _ in range(N)]
    # adj = [[] for _ in range(W*H)]
    # dx = [1, -1, 0, 0, -1, 1]
    # dy = [0, 0, 1, -1, -1, 1]

    # for i in range(H):
    #     for j in range(W):
    #         for k in range(6):
    #             y = i + dy[k]
    #             x = j + dx[k]
    #             if 0 <= y < H and 0 <= x < W:
    #                 adj[W * i + j].append(W * y + x)

    # ans = 0
    # for i in range(N - 1):
    #     s = XY[i][0] + XY[i][1]*W
    #     g = XY[i+1][0] + XY[i+1][1]*W
    #     queue = deque([s])
    #     visit = [-1] * (W*H)
    #     visit[s] = 0

    #     while queue and visit[g] < 0:
    #         now = queue.popleft()
    #         for u in adj[now]:
    #             if visit[u] < 0:
    #                 queue.append(u)
    #                 visit[u] = visit[now] + 1
    #     # print(s, g)
    #     ans += visit[g]
    ans = 0
    s = list(map(int, input().split()))
    for i in range(N - 1):
        g = list(map(int, input().split()))
        a = g[0] - s[0]
        b = g[1] - s[1]
        if a * b > 0:
            ans += abs(a) + abs(b) - min(abs(a), abs(b))
        else:
            ans += abs(a) + abs(b)
        s = g[:]
    print(ans)


if __name__ == "__main__":
    main()
