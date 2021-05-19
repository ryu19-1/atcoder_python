#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, W = map(int, input().split())
    V = N * 10**3
    INF = 10**12
    dp = [INF] * (V+1)# dp[i]: 価値の総和をiにするための重さの最小値
    dp[0] = 0

    for _ in range(N):
        w, v = map(int, input().split())
        for j in range(V,-1,-1):
            if j-v >= 0:
                dp[j] = min(dp[j],dp[j-v]+w)
    # print(dp)
    ans = -1
    for i in range(V+1):
        if dp[i] <= W:
            ans = i
    print(ans)

if __name__ == "__main__":
    main()
