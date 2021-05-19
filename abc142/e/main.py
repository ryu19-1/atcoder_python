#!/usr/bin/env python3


def main():
    N, M = map(int, input().split())
    INF = 10**12
    dp = [INF] * (1 << N)
    dp[0] = 0
    for i in range(M):
        a, b = map(int, input().split())
        c = list(map(lambda x: int(x) - 1, input().split()))
        mask = 0
        for cc in c:
            mask |= 1 << cc
        prev = dp[:]
        for j in range(1 << N):
            dp[j | mask] = min(prev[j | mask], prev[j] + a, dp[j | mask])
    ans = dp[-1]
    print(ans) if ans < INF else print(-1)

if __name__ == "__main__":
    main()
