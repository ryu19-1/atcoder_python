#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()
    reader = [None] * N
    for i in range(N):
        reader[i] = 'JOI'.index(S[i])
    # print(reader)
    dp = [[0]*8 for _ in range(N)]

    # 1日目の計算
    for i in range(1<<3):
        if i >> 0 & 1 and i >> reader[0] & 1:
            dp[0][i] = 1

    for i in range(1,N):
        for j in range(1<<3):# i-1日目の部員
            for k in range(1<<3):# i日目の部員
                if k >> reader[i] & 1:
                    # print(reader[i],k)
                    for l in range(3):
                        if (j >> l & 1) and (k >> l & 1):
                            dp[i][k] += dp[i-1][j]
                            dp[i][k] %= 10007
                            break
    print(sum(dp[N-1]) % 10007)

if __name__ == "__main__":
    main()
