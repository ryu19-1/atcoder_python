#!/usr/bin/env python3


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    # dp[i][j]: 仮に残りのケーキがi番目〜j番目で始めたとき、
    # JOI君の取り分の最大値
    # 円環を区間に潰したいので(j<i)の場合の対策として長さを２倍とる
    dp = [[0] * N for _ in range(N)]

    # あと1切れしかないとき、Nが奇数ならJOI君の取り分
    if N % 2 == 1:
        for i in range(N):
            dp[i][i] = A[i]

    for k in range(1,N):
        for i in range(N):# 既にとったケーキの数はk個
            if k % 2 != N % 2:  # JOI君のターン
                dp[i][(i+k)%N] = max(dp[(i+1)%N][(i+k)%N]+A[i], dp[i][(i+k-1)%N]+A[(i+k)%N])
            else:  # IOIちゃんのターン
                if A[i] > A[(i+k)%N]:
                    dp[i][(i+k)%N] = dp[(i+1)%N][(i+k)%N]
                else:
                    dp[i][(i+k)%N] = dp[i][(i+k-1)%N]
    ans = 0
    for i in range(N):# 最初にとるケーキを選択
        ans = max(ans, dp[i][(N-1+i)%N])
    print(ans)
    # print(dp)


if __name__ == "__main__":
    main()

