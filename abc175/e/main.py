#!/usr/bin/env python3

def main():
    R, C, K = map(int, input().split())
    S = [[0]*(C+1) for _ in range(R+1)]
    for i in range(K):
        r, c, v = map(int, input().split())
        S[r][c] = v

    dp = [[[0]*(C+1) for _ in range(R+1)] for _ in range(4)]

    for i in range(1,R+1):
        for j in range(1,C+1):
            V = S[i][j]
            for k in range(4):
                dp[0][i][j] = max(dp[0][i][j], dp[k][i-1][j])# アイテムを取らないで下に進む
                dp[1][i][j] = max(dp[1][i][j], dp[k][i-1][j] + V)# アイテムを取って下に進む
                dp[k][i][j] = max(dp[k][i][j], dp[k][i][j-1])# アイテムを取らないで右に進む
                if k > 0:
                    dp[k][i][j] = max(dp[k][i][j], dp[k-1][i][j-1] + V)# アイテムを取って右に進む
    ans = 0
    for k in range(4):
        ans = max(ans, dp[k][R][C])
    print(ans)

if __name__ == "__main__":
    main()