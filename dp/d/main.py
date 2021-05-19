#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, W = map(int, input().split())
    dp = [0]*(W+1)

    for _ in range(N):
        w, v = map(int, input().split())
        for j in range(W,-1,-1):# 後ろから更新しないとダメ
            if j - w >= 0:
                dp[j] = max(dp[j], dp[j-w]+v)
    print(dp[W])    

if __name__ == "__main__":
    main()
