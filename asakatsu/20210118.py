N = int(input())
excludeEdge = [[] for _ in range(N)]
if N % 2 == 0:
    for i in range(N // 2):
        excludeEdge[i].append(N - i - 1)
else:
    for i in range(N // 2):
        excludeEdge[i].append(N - 2 - i)

ans = []
for i in range(N):
    for j in range(i+1, N):
        if j in excludeEdge[i]:
            continue
        ans.append([i + 1, j + 1])
print(len(ans))
for a in ans:
    print(*a)
