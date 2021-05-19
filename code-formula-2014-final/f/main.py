ans = [None] * 101
ans[100] = [100, 100]
now = 99
prev = [200, 200]
cnt = 3
for i in range(9):
    tmp = now  # この回の正方形の大きさ
    tmpy = now
    tmpx = now
    # 縦横の座標
    for i in range(cnt // 2):
        ans[now] = [prev[0] + tmp, tmpy]
        now -= 1
        tmpy += tmp*2
        ans[now] = [tmpx, prev[0] + tmp]
        now -= 1
        tmpy += tmp*2
    # 対角線の座標
    ans[now] = [prev[0] + tmp, prev[0] + tmp]
    prev = [prev[0] + 2 * tmp, prev[0] + 2 * tmp]
    now -= 1
    cnt += 2
[print(ans[i]) for i in range(1, 101)]
