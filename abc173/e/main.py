N, K = map(int, input().split())
A = list(map(int, input().split()))
m = 10**9+7
pos = [*filter(lambda x: x>=0, A)]
neg = [*filter(lambda x: x<0, A)]
pos.sort(reverse=True)
neg.sort()

ans = 1
i,j = 0,0
while i+j < K:
    flag = True
    if i == len(pos):
        flag = False
    elif j == len(neg):
        flag = True
    elif pos[i] < -neg[j]:
        flag = False

    if flag:
        ans = ans * pos[i] % m
        i += 1
    else:
        ans = ans * neg[j] % m
        j += 1

if j % 2 == 0 or N==K:
    print(ans)
elif len(pos) == 0:
    ans = 1
    for i in range(K):
        ans = ans * neg[len(neg)-1-i] % m
    print(ans)
else:
    flag2 = True
    if i == 0:
        flag2 = True
    elif j == 0:
        flag2 = False
    elif i == len(pos):
        flag2 = False
    elif j == len(neg):
        flag2 = True
    elif pos[i-1]*pos[i] < neg[j-1]*neg[j]:
        flag2 = False

    if flag2:
        ans = (ans * pow(neg[j-1],m-2,m) % m) * pos[i] % m
    else:
        ans = (ans * pow(pos[i-1],m-2,m) % m) * neg[j] % m
    print(ans)