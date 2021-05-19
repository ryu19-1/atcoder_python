#!/usr/bin/env python3
from collections import deque


def main():
    H, W = map(int, input().split())
    S = [None for _ in range(H)]
    for i in range(H):
        S[i] = input()

    adj = [[] for _ in range(H * W)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                for k in range(4):
                    y = i + dy[k]
                    x = j + dx[k]
                    if 0 <= y < H and 0 <= x < W:
                        if S[y][x] == '.':
                            adj[W*i + j].append(W*y + x)

    # スタート
    ans = 0
    for i in range(H*W):
        queue = deque([i])
        visit = [-1] * (H * W)
        visit[i] = 0

        while queue:
            now = queue.popleft()
            for u in adj[now]:
                if visit[u] < 0:
                    queue.append(u)
                    visit[u] = visit[now] + 1
        ans = max(ans, max(visit))
    print(ans)


if __name__ == "__main__":
    main()
