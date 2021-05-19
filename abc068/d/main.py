K = int(input())
N = 50
print(N)
ans = [N-1+K//50-K % 50] * N
for i in range(K % 50):
    ans[i] += N
print(*ans)
