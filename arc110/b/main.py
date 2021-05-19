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
    T = input()
    if T == '1':
        print(2 * 10 ** 10)
    elif T in ['0', '11', '10']:
        print(10 ** 10)
    elif T in ['01', '101', '011', '1011']:
        print(10**10-1)
    else:
        cnt = T.count('110')
        tmp = T.split('110')
        if ''.join(tmp[1:-1]) != '':
            print(0)
            exit()

        if tmp[0] not in ['', '0', '10']:
            print(0)
            exit()
        else:
            if tmp[0] != '':
                cnt += 1

        if tmp[-1] not in ['', '1', '11']:
            print(0)
            exit()
        else:
            if tmp[0] != '':
                cnt += 1
        print(10**10-cnt+1)


if __name__ == "__main__":
    main()
