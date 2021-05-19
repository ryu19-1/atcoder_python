from heapq import heappop, heappush

H, W = map(int, input().split())
c =  [list(map(int, input().split())) for _ in range(10)]

# Dijkstra法で1からの距離を求める
adj = [[] for _ in range(n)]
INF = 10**12
q = [(0,1)] # 始点のコストとindex
d = [INF] * 10
d[1] = 0

while len(q) > 0:
    cost, u = heappop(q)
    print(u,c[u])
    for i in range(10):
        print(i,v)
        v = c[u][i]
        tmp = d[u] + cost
        if tmp < d[v]:
            d[v] = tmp
            heappush(q, (d[v], v))


A =  [0]*10
for i in range(H):
    tmp = list(map(int, input().split()))
    for j in range(W):
        if tmp[j] >= 0:
            A[tmp[j]] += 1

ans = 0
for i in range(10):
    ans += A[i]*d[i][1]
print(ans)