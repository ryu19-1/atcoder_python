N = int(input())
dame = set()
for i in range(N // 2):
    dame.add([i, (N//2)*2 - 1 - i])
ans = []
for i in range(N):
    for j in range(i + 1, N):
        if [i, j] not in dame:
            ans.append([i, j])
print(len(ans))
for a in ans:
    print(a[0]+1, a[1]+1)
