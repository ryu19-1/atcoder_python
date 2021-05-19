N, K = map(int, input().split())
A = list(map(int, input().split()))
xor = 0
for i in range(N):
    xor ^= A[i]
j = 0
now = 1
while now < xor:
    if xor >> j & 1:
        pass
    else:
        K -= now
    j += 1
    now *= 2
ans = 0
for i in range(N):
    ans += A[i] ^ K
print(ans)
