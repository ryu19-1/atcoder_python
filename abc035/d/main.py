from heapq import heappop, heappush

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
adj = [[] for _ in range(N)]
adj2 = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a-1].append((b-1, c))
    adj2[b-1].append((a-1, c))
 
INF = 10**12
q = [(0, 0)]
d = [0] + [INF] * (N-1)

while len(q) > 0:
    _, u = heappop(q)
    for v, c in adj[u]:
        tmp = d[u] + c
        if tmp < d[v]:
            d[v] = tmp
            heappush(q, (d[v], v))

q = [(0, 0)]
d2 = [0] + [INF] * (N-1)

while len(q) > 0:
    _, u = heappop(q)
    for v, c in adj2[u]:
        tmp = d2[u] + c
        if tmp < d2[v]:
            d2[v] = tmp
            heappush(q, (d2[v], v))

ans = 0
for i in range(N):
    ans = max(ans, A[i] * (T - d[i] - d2[i]))
print(ans)
