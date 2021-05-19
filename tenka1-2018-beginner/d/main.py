#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    if N == 1:
        print('Yes')
        print(2)
        print(1,1)
        print(1,1)
        exit()
    i = 3
    l = 2
    while i <= 10**5:
        if i == N:
            break
        else:
            l += 1
            i += l
    else:
        print('No')
        exit()

    # 長さl, k = 2N/l個の配列が答え
    ans = [[1,2],[2,3],[3,1]]
    now = 3# 今使ってる最大の数字
    M = 2# 今の長さ
    k = 2*N//l
    while M < l:
        for j in range(M+1):
            ans[j].append(now+1+j)
        ans.append(list(range(now+1,now+2+M)))
        now += M+1
        M += 1
    print('Yes')
    print(k)
    for i in range(k):
        print(l,*ans[i])



if __name__ == "__main__":
    main()
