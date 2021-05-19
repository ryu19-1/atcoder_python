from collections import deque

N = int(input())
adj = [[] for _ in range(N)]
for i in range(N):
    k, *c = list(map(int, input().split()))
    for cc in c:
        adj[i].append(cc)
# print(adj)

K = 0
tmp = 1
while tmp <= N:
    tmp *= 2
    K += 1
# 前処理
# parent[k][i]: 接点iの2^k個祖先
parent = [[None]*N for _ in range(K)]

# それぞれの接点の深さを調べる
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
# print(depth)
for k in range(1, K):
    for i in range(N):
        parent[k][i] = parent[k - 1][parent[k - 1][i]]

# print(parent)
Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    if depth[u] > depth[v]:
        u, v = v, u

    # print(depth[v], depth[u], v, u)
    # vをuと同じ深さまで探索する
    diff = depth[v] - depth[u]
    for i in range(K):
        if diff >> i & 1:
            v = parent[i][v]
    # print(depth[v], depth[u], v, u)
    if u == v:
        print(u)
        continue

    # 二分探索で祖先が共通になる直前の接点を調べる
    for i in range(K - 1, -1, -1):
        if parent[i][u] != parent[i][v]:
            # 異なるなら両方をそこまで進める
            u = parent[i][u]
            v = parent[i][v]
    print(parent[0][u])
