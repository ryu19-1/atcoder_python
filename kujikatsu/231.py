N = input()
L = len(N)
ans = 0
# お釣りなしで払う場合
for i in range(L):
    ans += int(N[i])

# dp[i][k]: 上からi桁まで見たときの最小値(k=0: ぴったり払っている/k=1: 1だけ余分に払っている)
dp = [0] * 2
for i in range(L):
    s = int(N[i])
    nextdp = [None, None]
    nextdp[0] = min(dp[0] + s, dp[1] + 10 - s)
    nextdp[1] = min(dp[0] + s+1, dp[1] + 9 - s)
    dp = nextdp[:]
print(dp)
