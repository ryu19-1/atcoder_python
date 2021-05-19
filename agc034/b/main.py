#!/usr/bin/env python3
from itertools import accumulate

s = input()
l = s.split('BC')[:-1]
l = l[::-1]

ans = 0
i = 0

while i < len(l):
    anum = []
    flag = True
    while flag and i < len(l):
        M = len(l[i])
        tmp = 0
        for j in range(M):
            if l[i][M-j-1] == 'A':
                tmp += 1
            else:
                flag = False
                break
        anum.append(tmp)
        if flag:
            i += 1
    ans += sum(accumulate(anum[::-1]))
    i += 1
print(ans)
