#!/usr/bin/env python3


def check(S, cnt):
    global ans
    # print(S, cnt)
    if S == B2:
        # print(S, cnt)
        ans = min(ans, cnt)
    elif cnt < 3:
        for i in range(M):
            for j in range(i + 1, M):
                T = S[:]
                T[i], T[j] = T[j], T[i]
                check(T, cnt+1)


A = list(input())
B = list(input())
if sorted(A) != sorted(B):
    print('NO')
    exit()

N = len(A)
A2 = []
B2 = []
for i in range(N):
    if A[i] != B[i]:
        A2.append(A[i])
        B2.append(B[i])

if len(A2) > 6:
    print('NO')
    exit()

flag = False
for i in range(N):
    for j in range(i + 1, N):
        if A[i] == A[j]:
            flag = True
            break

M = len(A2)
ans = 10**12
check(A2, 0)
# print(ans)
if flag:
    if ans <= 3:
        print('YES')
    else:
        print('NO')
else:
    if ans == 1 or ans == 3:
        print('YES')
    else:
        print('NO')
