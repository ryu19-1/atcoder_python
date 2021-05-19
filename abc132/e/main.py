from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(3*N)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    adj[3*u].append(3*v+1)
    adj[3*u+1].append(3*v+2)
    adj[3*u+2].append(3*v)

S, T = map(lambda x: int(x) - 1, input().split())

queue = deque([3*S])
visit = [-1] * (3*N)
visit[3*S] = 0

while queue:
    now = queue.popleft()
    for u in adj[now]:
        if visit[u] < 0:
            queue.append(u)
            visit[u] = visit[now] + 1

print(visit[3*T]//3)
