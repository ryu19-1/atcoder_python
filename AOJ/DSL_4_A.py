N = int(input())
x1 = [None] * N
x1 = [None] * N
y1 = [None] * N
y2 = [None] * N

for i in range(N):
    x1[i], y1[i], x2[i], y2[i] = map(int, input().split())

x = sorted(x1 + x2)
y = sorted(y1 + y2)
ans = 0
for i in range(2 * N - 1):
    for j in range(2 * N - 1):
        for k in range(N):
            if x1[k] <= x[i] and x[i + 1] <= x2[k] and y1[k] <= y[j] and y[j + 1] <= y2[k]:
                ans += (x2[k]-x1[k]) * (y2[k]-y1[k])
                break
print(ans)
