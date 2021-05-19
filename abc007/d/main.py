#!/usr/bin/env python3


def cal_pattern(N):
    N = str(N)
    dp = [[0] * 2 for _ in range(20)]
    dp[0][1] = 1
    M = len(N)
    check = [0, 1, 2, 3, 4, 4, 5, 6, 7, 8]  # 1 ->0 遷移の個数
    for i in range(M):
        # 1 -> 1の遷移
        if N[i] != '4' and N[i] != '9':
            dp[i+1][1] += dp[i][1]

        # 1 -> 0の遷移
        dp[i + 1][0] += dp[i][1] * check[int(N[i])]

        # 0 -> 0の遷移
        dp[i + 1][0] += dp[i][0] * 8
    return sum(dp[M])


def main():
    A, B = map(int, input().split())
    print(B-A+1 - (cal_pattern(B)-cal_pattern(A-1)))


if __name__ == "__main__":
    main()
