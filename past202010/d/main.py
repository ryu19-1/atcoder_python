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
    S = input()
    index = [-1, N]
    for i in range(N):
        if S[i] == '#':
            index.append(i)
    index.sort()
    # print(index)
    check = []
    for i in range(len(index)-1):
        check.append(index[i + 1] - index[i] - 1)
    M = len(check)

    ans = [1000, 1000]
    for x in range(100):
        for y in range(100):
            flag = True
            for i in range(M):
                if i == 0 and x < check[i]:
                    flag = False
                    break
                elif i == M - 1 and y < check[i]:
                    flag = False
                    break
                else:
                    if x + y < check[i]:
                        flag = False
                        break
            if flag and ans[0]+ans[1] > x+y:
                ans = [x, y]
    print(*ans)


if __name__ == "__main__":
    main()
