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
    # A = 'abracadabra'
    # a = set()
    # a.add(A)
    # for i in range(11):
    #     for j in range(i,11):
    #         tmp = A[i:j+1][::-1]
    #         if i > 0:
    #             tmp = A[:i] + tmp
    #         if j < 10:
    #             tmp = tmp + A[j+1:]
    #         if tmp in a:
    #             print(i,j,tmp)
    #         a.add(tmp)
    # print(len(a))
    A = input()
    N = len(A)
    l = Counter(A)
    ans = N*(N+1)//2 + 1 - N
    for x in l.values():
        ans -= x*(x-1)//2
    print(ans)

if __name__ == "__main__":
    main()
