#!/usr/bin/env python3
from collections import deque


def main():
    N = int(input())
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        x, y = map(lambda x: int(x) - 1, input().split())
        adj[x].append(y)
        adj[y].append(x)

    K = 0
    tmp = 1
    while tmp <= N:
        tmp *= 2
        K += 1

    # 前処理
    parent = [[None] * N for _ in range(K)]

    queue = deque([0])
    depth = [-1] * N
    depth[0] = 0
    parent[0][0] = 0

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if depth[u] < 0:
                queue.append(u)
                depth[u] = depth[now] + 1
                parent[0][u] = now

    for k in range(1, K):
        for i in range(N):
            parent[k][i] = parent[k - 1][parent[k - 1][i]]

    Q = int(input())
    for _ in range(Q):
        a, b = map(lambda x: int(x) - 1, input().split())
        if depth[a] > depth[b]:
            a, b = b, a

        ans = 1 + depth[a] + depth[b]
        diff = depth[b] - depth[a]
        for i in range(K):
            if diff >> i & 1:
                b = parent[i][b]

        if a == b:
            d = a
        else:
            for i in range(K - 1, -1, -1):
                if parent[i][a] != parent[i][b]:
                    a = parent[i][a]
                    b = parent[i][b]
            d = parent[0][a]

        print(ans - 2*depth[d])


if __name__ == "__main__":
    main()
