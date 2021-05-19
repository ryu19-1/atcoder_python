#!/usr/bin/env python3
from bisect import bisect_left
from itertools import permutations

INF = 10**12


def main():
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    LV = [[0, 0]]
    for _ in range(M):
        l, v = map(int, input().split())
        LV.append([v, l])
    LV.sort()
    V = [0]
    LV2 = [[0, 0]]
    now = 0
    for a in LV:
        if a[1] > now:
            now = a[1]
            LV2.append(a)
            V.append(a[0])
    if V[1] < max(w):
        print(-1)
        exit()
    ans = INF
    # N!通りを全探索する
    for p in permutations(range(N)):
        dp = [0] * N
        dp[0] = 0
        for i in range(1, N):
            wsum = w[p[i]]
            for j in range(i-1, -1, -1):
                wsum += w[p[j]]
                d = bisect_left(V, wsum)
                dp[i] = max(dp[i], dp[j]+LV2[d-1][1])
        ans = min(ans, dp[N - 1])
    print(ans)


if __name__ == "__main__":
    main()
