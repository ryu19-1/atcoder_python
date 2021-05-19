N, M, K = map(int, input().split())
S = [list(input()) for _ in range(N)]
count = [[[0]*(M+1) for _ in range(N+1)] for _ in range(10)]
for i in range(N):
    for j in range(M):
        count[int(S[i][j])][i+1][j+1] += 1

for k in range(10):
    for i in range(N):
        for j in range(M + 1):
            if j < M:
                count[k][i + 1][j + 1] += count[k][i + 1][j]
            count[k][i + 1][j] += count[k][i][j]

for n in range(min(N, M), 0, -1):
    for i in range(N - n + 1):
        for j in range(M - n + 1):
            for k in range(10):
                cnt = count[k][i + n][j + n] - count[k][i +
                                                        n][j] - count[k][i][j + n] + count[k][i][j]
                if cnt + K >= n * n:
                    print(n)
                    exit()
