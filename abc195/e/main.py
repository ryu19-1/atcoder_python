#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**6)


def DFS(i, now):
    if now in dic:
        return dic[now]

    if i == N:
        # 7の倍数か判定する
        res = int(now) % 7 == 0
        dic[now] = res
        return res
    else:
        # print(now)
        if X[i] == 'T':
            # now + '0'と now + S[i]のどれかが7の倍数ならかち
            if int(now) % 7 == 0:
                if DFS(i + 1, '0') or DFS(i + 1, S[i]):
                    return True
                else:
                    return False
            else:
                if DFS(i + 1, now + '0') or DFS(i + 1, now + S[i]):
                    return True
                else:
                    return False
        else:
            if int(now) % 7 == 0:
                if (not DFS(i + 1, '0')) or (not DFS(i + 1, S[i])):
                    return False
                else:
                    return True
            else:
                if (not DFS(i + 1, now + '0')) or (not DFS(i + 1, now + S[i])):
                    return False
                else:
                    return True


N = int(input())
S = input()
X = input()
dic = {}
ans = DFS(0, '0')
if ans:
    print('Takahashi')
else:
    print('Aoki')
