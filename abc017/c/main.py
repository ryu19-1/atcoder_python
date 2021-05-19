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
    # それぞれの宝石を使わない場合に貪欲に遺跡を選んだ最大値を探索
    # 最大値の計算にO(N)かかるので、逆にその宝石を使う遺跡のスコアを合計から引けばO(1)でもとまる
    #imos法
    N, M = map(int, input().split())
    imos = [0] * (M+1)
    ans = 0
    for _ in range(N):
        l, r, s = map(int, input().split())
        imos[l-1] += s
        imos[r] -= s
        ans += s
    imos = [*accumulate(imos)]
    print(ans - min(imos[:-1:]))

if __name__ == "__main__":
    main()