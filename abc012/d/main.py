#!/usr/bin/env python3

def main():
    N, M = map(int, input().split())
    INF = 10**12
    dp = [[INF] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0

    for _ in range(M):
        a, b, t = map(int, input().split())
        dp[a-1][b-1] = t
        dp[b-1][a-1] = t
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                #if dp[i][k] < INF and dp[k][j] < INF:
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    
    ans = INF
    for i in range(N):
        ans = min(ans, max(dp[i]))
    print(ans)

if __name__ == "__main__":
    main()
