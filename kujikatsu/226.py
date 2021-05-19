N = int(input())
ans = 0
now = 1
while ans + now <= N:
    ans += now
    now += 1
print(ans, N-ans)
