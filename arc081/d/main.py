N, S1, S2 = open(0)
N = int(N)
m = 10**9+7

i = 0
dominos = []
while i < N:
    if S1[i] == S2[i]:# 縦のドミノ
        dominos.append(0)
        i += 1
    else:
        dominos.append(1)
        i += 2

ans = 3
for i in range(len(dominos)):
    if dominos[i] == 0:
        if i > 0 and dominos[i-1] == dominos[i]:
            ans = ans * 2 % m
    else:
        if i > 0 and dominos[i-1] == dominos[i]:
            ans = ans * 3 % m
        else:
            ans = ans * 2 % m
print(ans)