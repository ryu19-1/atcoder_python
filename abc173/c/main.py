#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    H, W, K = map(int, input().split())
    c = [None] * H
    for i in range(H):
        c[i] = input()

    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            tmp = 0
            # print(i,j)
            for ii in range(H):
                for jj in range(W):
                    # print(ii,jj)
                    if c[ii][jj] == '#':
                        # print((i >> ii)&1,)
                        if ((i >> ii)&1) or ((j >> jj)&1):
                            pass
                        else:
                            tmp += 1
            # print(tmp)
            if tmp == K:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
