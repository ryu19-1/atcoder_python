N, M = map(int, input().split())
INF = 10**18
g = [[(INF,INF)]*N for _ in range(2**N)]
for i in range(M):
    s, t, d, time = map(int, input().split())
    g[s-1][t-1] = (d, time)
    g[t-1][s-1] = (d, time)

dp = [[[INF,0]]*N for _ in range(2**N)]
dp[0][0] = [0,1]

for s in range(2**N):
    for j in range(N):
        if (s >> j & 1) == 0:
            for i in range(N):
                J = s|1<<j
                x,y = dp[s][i]
                u,v = g[i][j]
                p=x+u
                f=dp[J][j][0]
                if p <= v:
                    if p == f:
                        dp[J][j][1] += y
                    elif p < f:
                        dp[J][j] = [p,y]
if dp[2**N-1][0][0] == INF:
    print('IMPOSSIBLE') 
else:
    print(*dp[2**N-1][0])