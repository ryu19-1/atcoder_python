#!/usr/bin/env python3


def main():
    N, L = map(int, input().split())
    x = set(map(int, input().split()))
    T = list(map(int, input().split()))
    # dp[i]: 距離iに到達する最短時間
    INF = 10**18
    dp = [INF] * (L+4)
    dp[0] = 0
    for i in range(L):
        tmp = dp[i]
        if i in x:  # ハードルあり
            tmp += T[2]
        # 行動1の場合
        dp[i+1] = min(dp[i+1], tmp + T[0])
        # 行動2の場合
        if i+1 == L:
            dp[i+1] = min(dp[i+1], tmp +  T[0]//2 + T[1]//2)
        dp[i+2] = min(dp[i+2], tmp + T[0] + T[1])
        # 行動3の場合
        if i+2 == L:
            dp[i+2] = min(dp[i+2], tmp +  T[0]//2 + (T[1]*3)//2)
        elif i+3 == L:
            dp[i+3] = min(dp[i+3], tmp + T[0]//2 + (T[1]*5)//2)
        dp[i+4] = min(dp[i+4], tmp + T[0] + T[1]*3)
    print(dp[L])


if __name__ == "__main__":
    main()
