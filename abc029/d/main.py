N = int(input())
ans = 0
L = len(str(N))
for i in range(1, L+1):
    e = pow(10, i-1)
    d = e*10
    res = N // d * e
    tmp = N % d - e + 1
    res += min(max(0, tmp), e)
    ans += res
print(ans)
