from collections import deque

N = int(input())
S = [input() for _ in range(N)]
adj = [[] for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if S[i][j] == '1':
            adj[i].append(j)
            adj[j].append(i)
ans = -1
for i in range(N):
    queue = deque([i])
    visit = [-1] * N
    visit[0] = 1

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                visit[u] = visit[now] + 1

    flag = True
    for j in range(N):
        for k in range(N):
            if S[j][k] == '1':
                if abs(visit[j] - visit[k]) != 1:
                    flag = False
                    break
    if flag:
        ans = max(ans, max(visit))
print(ans)
# INF = 10 ** 12
# adj = [[INF] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if int(S[i][j]):
#             adj[i][j] = int(S[i][j])

# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             if i == j:
#                 continue
#             adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
# ans = 0
# for i in range(N):
#     for
# print(adj)
