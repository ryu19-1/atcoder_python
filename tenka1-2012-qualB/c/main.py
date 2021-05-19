#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

def main():
    N = int(input())
    fromTo = []
    for _ in range(N):
        Ts, Te = input().split()
        start = int(Ts.split(':')[0]) * 60 + int(Ts.split(':')[1])
        end = int(Te.split(':')[0]) * 60 + int(Te.split(':')[1])
        fromTo.append((start,end))

    fromTo.sort()

    check = [[1]*N for _ in range(N)]

    # check[i][j]: i人目とj人目が同じ席を使用可能か
    for i in range(N):
        timezone = [0]*(1440)
        for j in range(fromTo[i][0],fromTo[i][1]):
            timezone[j%1440] += 1

        for j in range(i+1,N):
            for k in range(fromTo[j][0],fromTo[j][1]):
                if timezone[k%1440]:# 既にi番目の人が座っている
                    check[i][j] = check[j][i] = 0
                    break
    
    # sortしているから開始時間が早い順に座らせ、シェア可能な人を貪欲に選んで良い
    ans = 0
    remind = [*range(N)]

    while remind:
        ans += 1# remind[0]番目の人がこの席に座るとする
        
        share = []# 今回座る人と席をシェアする人達
        nextRemind = []# 次の席に座る候補の人達

        for i in remind:
            for j in share:
                if not check[i][j]:
                    nextRemind.append(i)
                    break
            else:# for文でbreakしなかったらshareに追加
                share.append(i)
        remind = nextRemind
    print(ans)

if __name__ == "__main__":
    main()
