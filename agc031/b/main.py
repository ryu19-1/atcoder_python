#!/usr/bin/env python3
from bisect import bisect_left

def main():
    N, *C = map(int,open(0))
    M = max(C)
    m = 10**9+7
    # place[j]: i番目の石の位置を保持(1-index)
    place = [[] for _ in range(M+1)]
    for i in range(N):
        place[C[i]].append(i+1)
    # dp[i]: 最初からi個の石までで条件を満たす塗り方の総数
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1,N+1):
        # 特に操作しない場合
        dp[i] += dp[i-1]
        dp[i] %= m
        
        # 操作する場合
        # 今見ているi番目の石が同じ色の石の集まりの中で何番目か
        j = bisect_left(place[C[i-1]],i)
        if j > 0:
            k = place[C[i-1]][j-1]# 同色でjより１つ前の石の位置
            if i-k > 1:
                dp[i] += dp[k]
                dp[i] %= m
    print(dp[N])

if __name__ == "__main__":
    main()
    