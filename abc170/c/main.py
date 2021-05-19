X, N = map(int, input().split())
p = list(map(int, input().split()))

ans = 0
absAns = 1000
for i in range(0,102):
    if i not in p:
        if absAns > abs(X - i):
            absAns = abs(X - i)
            ans = i
print(ans)