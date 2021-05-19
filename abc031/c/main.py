#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = - 10**12
    for i in range(N):# 高橋君の選択
        tmp = -10**12
        l = 0
        r = 0
        for j in range(N):
            if i == j:
                continue
            tmpi = min(i,j)
            tmpj = max(i,j)
            hoge = sum(a[tmpi:tmpj+1][1::2])
            if hoge > tmp:
                tmp = hoge
                l = tmpi
                r = tmpj+1
        # print(a[l:r])
        ans = max(ans, sum(a[l:r][::2]))
    print(ans)



if __name__ == "__main__":
    main()
