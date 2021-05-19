N, A, B = map(int, input().split())

v = list(map(int, input().split()))
# dp[i][j]: i番目までからj個選んだときの最大個数の場合のかず
dp = [(0, 0)] * (N + 1)
dp[0] = (0, 1)

for i in range(1, N+1):
    for j in range(i-1, -1, -1):
        if dp[j + 1][0] == dp[j][0] + v[i-1]:
            dp[j + 1] = (dp[j+1][0], dp[j+1][1]+dp[j][1])
        elif dp[j + 1][0] < dp[j][0] + v[i-1]:
            dp[j+1] = (dp[j][0] + v[i-1], dp[j][1])
print(dp)
ans = [-1, -1]
tmp = -1
for i in range(A, B + 1):
    # print(dp[N][i])
    if ans[0]*tmp < dp[i][0]:
        ans = [dp[i][0], dp[i][1]]
        tmp = i
    elif ans[0]*tmp == dp[i][0]:
        ans[1] += dp[i][1]
print(ans[0])
print(ans[1])
