import sys
sys.setrecursionlimit(10**7)


def dfs(i, j):
    if root[i][j] != -1:
        return root[i][j]
    res = 1
    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]
        if 0 <= x < W and 0 <= y < H and a[i][j] < a[y][x]:
            res += dfs(y, x)
            res %= mod
    root[i][j] = res
    return res


H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
mod = 10**9 + 7

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = 0
root = [[-1]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        ans += dfs(i, j)

print(ans % mod)
