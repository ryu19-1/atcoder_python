N = int(input())
a = list(map(int, input().split()))
suma = sum(a)
r = 0
sumnow = 0
ans = 10**12
for l in range(N):
    while r < N and 2 * (sumnow + a[r]) < suma:
        sumnow += a[r]
        ans = min(ans, abs(2 * sumnow - suma))
        r += 1
    if r < N:
        ans = min(ans, abs(2 * (sumnow+a[r]) - suma))
    if l == r:
        r += 1
    else:
        sumnow -= a[l]
print(ans)
