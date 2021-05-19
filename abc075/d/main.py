N, K = map(int, input().split())
x = [None] * N
y = [None] * N

for i in range(N):
    x[i], y[i] = map(int, input().split())

ans = 10**20
sx = sorted(x)
sy = sorted(y)
# 長方形の辺の位置で全探索
for i in range(N):# 左
    for j in range(i+1,N):# 右
        for k in range(N):# 上
            for l in range(k+1,N):# 下
                count = 0
                # 点が長方形に含まれるか確認
                for m in range(N):
                    if sx[i] <= x[m] <= sx[j] and sy[k] <= y[m] <= sy[l]:
                        count += 1
                if count >= K:
                    ans = min(ans, (sx[j]-sx[i]) * (sy[l]-sy[k]))
print(ans)