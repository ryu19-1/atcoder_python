from itertools import permutations

N, C = map(int, input().split())

D = [None] * C
for i in range(C):
    D[i] = list(map(int, input().split()))

c = [None] * N
for i in range(N):
    c[i] = list(map(int, input().split()))

# (i+j)%3 = 0,1,2 のそれぞれで初期マスの色をカウント
t = [[0]*C for _ in range(3)]
for i in range(N):
    for j in range(N):
        t[(i+j)%3][c[i][j]-1] += 1

ans = 0

# 塗り分けの順列総数
for p in permutations(range(C),3):
    tmp = 0
    for i in range(C):
        tmp += D[i][p[0]] * t[0][i]
        tmp += D[i][p[1]] * t[1][i]
        tmp += D[i][p[2]] * t[2][i]
    ans = min(ans,tmp)

print(ans)