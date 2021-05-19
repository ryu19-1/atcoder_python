from bisect import bisect_left

N = int(input())
a = [int(input()) for _ in range(N)]
INF = 10**12
dp = [INF] * N

for i in range(N):
    d = bisect_left(dp, a[i])
    dp[d] = a[i]
print(len(filter(lambda x: x < INF, dp)))
