from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
for i in range(N*M):
    if S[i//M][i % M] == '.':
        start = i
        break
ans = 0
for i in range(N):
    for j in range(M):
        if S[i][j] == '.':
            continue
        T = deepcopy(S)
        T[i][j] = '.'
        adj = [[] for _ in range(N*M)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for ii in range(N):
            for jj in range(M):
                if T[ii][jj] == '#':
                    continue
                for k in range(4):
                    y = ii + dy[k]
                    x = jj + dx[k]
                    if 0 <= y < N and 0 <= x < M and T[y][x] == '.':
                        adj[M * ii + jj].append(M * y + x)

        queue = deque([start])
        visit = [-1] * (N*M)
        visit[start] = 1

        while queue:
            now = queue.popleft()
            for u in adj[now]:
                if visit[u] < 0:
                    queue.append(u)
                    visit[u] = visit[now]
        for ii in range(N*M):
            if T[ii // M][ii % M] == '.' and visit[ii] == -1:
                break
        else:
            ans += 1
print(ans)
