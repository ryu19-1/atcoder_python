N = int(input())
A = [int(input()) for _ in range(N)]
dic = {}
AA = sorted(A)
for i in range(N):
    dic[AA[i]] = i
ans = 0
for a in A[::2]:
    if dic[a] % 2 == 1:
        ans += 1
print(ans)
