N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]
INF = 10**12
dp = [0] + [INF]*N
for i in range(M):
    for j in range(N-1,-1,-1):
        dp[j+1] = min(dp[j+1], dp[j]+C[i]*D[j])
print(dp[N])