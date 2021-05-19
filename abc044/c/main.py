#!/usr/bin/env python3


def main():
    N, A = map(int, input().split())
    x = list(map(int, input().split()))
    X = 50
    dp = [[[0]*(N*X +1) for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for j in range(1,N+1):
        for k in range(N+1):
            for s in range(N*X+1):
                if s >= x[j-1] and k >= 1:
                    dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-x[j-1]]
                else:# x[j]を選ぶと合計sにできない
                    dp[j][k][s] = dp[j-1][k][s]
    ans = 0
    for i in range(N):
        ans += dp[N][i+1][(i+1)*A]
    print(ans)

if __name__ == "__main__":
    main()
