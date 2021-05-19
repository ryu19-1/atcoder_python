H, W = map(int, input().split())
A = [None]*H
for i in range(H):
    A[i] = list(map(int, input().split()))
B = [None]*H
for i in range(H):
    B[i] = list(map(int, input().split()))

# C: A-Bの絶対値を持つ
C = [[None]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        C[i][j] = abs(A[i][j]-B[i][j])

K = 80*(H+W-1)//2 + 1# 80*(H+W-1)の半分を超えるのは無駄
dp = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]# 答えから80*(H+W-1)を引く
dp[0][0][C[0][0]] = 1

for i in range(H):
    for j in range(W):
        for k in range(K+1):
            if i and dp[i-1][j][k]:
                if k+C[i][j] < K:
                    dp[i][j][k+C[i][j]] = 1
                dp[i][j][abs(k-C[i][j])] = 1
            if j and dp[i][j-1][k]:
                if k+C[i][j] < K:
                    dp[i][j][k+C[i][j]] = 1
                dp[i][j][abs(k-C[i][j])] = 1

for k in range(K+1):
    res = dp[H-1][W-1][k]
    if res:
        print(k)
        break