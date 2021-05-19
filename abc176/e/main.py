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
    H, W, M = map(int, input().split())
    h = [0] * H
    w = [0] * W
    hw = set()
    for i in range(M):
        tmph, tmpw = map(lambda x: int(x)-1, input().split())
        h[tmph] += 1
        w[tmpw] += 1
        hw.add((tmph,tmpw))
    # 最大値より1だけ小さくなる物が候補
    HMAX = max(h)
    h0 = []
    for i in range(H):
        if h[i] == HMAX:
            h0.append(i)

    WMAX = max(w)
    w0 = []
    for i in range(W):
        if w[i] == WMAX:
            w0.append(i)

    ans = 0
    for i in h0:
        for j in w0:
            if (i,j) not in hw:
                print(HMAX+WMAX)
                exit()
    print(HMAX+WMAX-1)

if __name__ == "__main__":
    main()
