N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            a = xy[i][0] - xy[k][0]
            b = xy[i][1] - xy[k][1]
            c = xy[j][0] - xy[k][0]
            d = xy[j][1] - xy[k][1]
            S = abs(a * d - b * c)
            if S > 0 and S % 2 == 0:
                ans += 1
print(ans)
