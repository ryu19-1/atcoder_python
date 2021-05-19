from bisect import bisect_right

#!/usr/bin/env python3
N = int(input())
P = list(map(int, input().split()))
check = 1  # 今場所が合っていない最小の数
used = [True] * N
ans = []
iti = {}
for i in range(N):
    iti[P[i]] = i+1
# print(iti)
while check <= N:
    # print(check, P, iti)
    d = iti[check]-1
    # print(d)
    # d = P.index(check)
    if d == check - 1:  # 場所が合っている
        check += 1
    else:
        if used[d]:
            # print(d)
            ans.append(d)
            iti[check] = d
            iti[P[d-1]] = d+1
            P[d - 1], P[d] = P[d], P[d - 1]
            used[d] = False
        else:
            print(-1)
            exit()
if len(ans) != N-1:
    print(-1)
    exit()
[print(a) for a in ans]
