A, B = map(int, input().split())
ans = 0
X = (4 - A % 4) % 4
for i in range(X):
    ans ^= (A + i)

Y = B % 4
for i in range(Y + 1):
    ans ^= (B - i)

print(ans)
