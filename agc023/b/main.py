#!/usr/bin/env python3


def f(i, j, a, b):
    return (i+a) % N, (j+b) % N


N = int(input())
S = [input() for _ in range(N)]
ans = 0
for a in range(1):
    for b in range(N):
        flag = True
        for i in range(N):
            for j in range(i + 1, N):
                # (i,j)をy方向にa,x方向にbだけ平行移動
                y1, x1 = f(i, j, a, b)
                y2, x2 = f(j, i, a, b)
                if S[y1][x1] != S[y2][x2]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans += 1
print(ans*N)
