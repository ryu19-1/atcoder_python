#!/usr/bin/env python3
import copy

H, W, K = map(int, input().split())
if K > W:
    exit(print(0))

# 現在の盤面を生成する
c = [[] for _ in range(W)]
for i in range(H):
    S = input()
    for j in range(W):
        c[j].append(int(S[j]))

for j in range(W):
    c[j] = c[j][::-1]

# 連鎖消滅後の得点を計算する
def cal_score(c,score,loop):
    # 消滅
    nextc = []
    for j in range(W):
        num0 = c[j].count(0)
        tmp = [*filter(lambda x: x>0,c[j])]
        nextc.append(tmp+[0]*num0)

    # 連鎖
    res = 0# 追加得点
    for i in range(H):
        j = 0
        while j < W:
            seq = 1
            while j<W-1 and nextc[j][i] == nextc[j+1][i] > 0:
                seq += 1
                j += 1
            if seq >= K:
                res += seq * nextc[j][i]
                for k in range(j-seq+1,j+1):
                    nextc[k][i] = 0
            j += 1
    if res == 0:
        return score
    else:
        return cal_score(nextc,score+res*pow(2,loop),loop+1)
    

ans = 0
for p in range(H):
    for q in range(W):
        cc = copy.deepcopy(c)
        cc[q][p] = 0
        z = cal_score(cc,0,0)
        ans = max(ans, z)
print(ans)