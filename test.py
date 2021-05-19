N = int(input())
H = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
H = [[0] * (N+2)] + H + [[0] * (N+2)]
# print(H)
ans = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(1, N+1):
    for j in range(1, N+1):
        now = H[i][j]
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if H[y][x] >= now:
                break
        else:
            ans.append(now)
for a in sorted(ans, reverse=True):
    print(a)
