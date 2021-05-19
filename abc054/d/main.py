#!/usr/bin/env python3
def main():
    N, Ma, Mb = map(int, input().split())
    a = [None] * N
    b = [None] * N
    c = [None] * N
    for i in range(N):
        a[i], b[i], c[i] = map(int, input().split())

    INF = 10**12
    dp = [[INF] * 401 for _ in range(401)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(400,-1,-1):# 後ろから更新すること
            for k in range(400,-1,-1):
                if j - a[i] >= 0 and k - b[i] >= 0:
                    dp[j][k] = min(dp[j][k], dp[j-a[i]][k-b[i]]+c[i])
    
    ans = INF
    for j in range(400):
        for k in range(400):
            if j*Mb == k*Ma != 0:
                ans = min(ans,dp[j][k])
    print(ans) if ans < INF else print(-1)

if __name__ == "__main__":
    main()