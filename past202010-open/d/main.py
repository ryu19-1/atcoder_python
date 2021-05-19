N = int(input())
S = input()
index = [-1]+[*filter(lambda i:S[i] == '#', range(N))]+[N]
check = []
for i in range(len(index)-1):
    check.append(index[i + 1] - index[i] - 1)
M = len(check)

ans = [N, N]
for x in range(N+1):
    for y in range(N+1):
        flag = True
        for i in range(M):
            if i == 0 and x < check[i]:
                flag = False
                break
            elif i == M - 1 and y < check[i]:
                flag = False
                break
            else:
                if x + y < check[i]:
                    flag = False
                    break
        if flag and ans[0]+ans[1] > x+y:
            ans = [x, y]
print(*ans)
