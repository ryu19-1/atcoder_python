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
    S = [input() for _ in range(N)]
    dic = set()
    dic2 = set()
    for i in range(N):
        if S[i][1:] in dic or S[i] in dic2:
            continue
        else:
            if S[i][0] == '!':
                dic.add(S[i][1:])
            else:
                dic2.add(S[i])
    if len(dic & dic2) > 0:
        print(list(dic & dic2)[0])
    else:
        print('satisfiable')


if __name__ == "__main__":
    main()
