H, W, K = map(int, input().split())
dp = [[0] * W for _ in range(H + 1)]
dp[0][K - 1] = 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34]
m = 10**9 + 7
for i in range(H):
    for j in range(W):
        # 線を引かない場合
        dp[i+1][j] += (dp[i][j] * a[j] % m) * a[W-j-1] % m
        dp[i+1][j] %= m
        # j-1 と jの間に線を引いた時
        if j > 0:
            dp[i+1][j-1] += (dp[i][j] * a[j-1] % m) * a[W-j-1] % m
            dp[i + 1][j - 1] %= m
        # j と j+1の間に線を引いた時
        if j < W - 1:
            dp[i+1][j+1] += (dp[i][j] * a[j] % m) * a[W-j-2] % m
            dp[i+1][j+1] %= m
print(dp[H][0])
