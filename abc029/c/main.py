#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def saiki(ans,i):
    if i == 1:
        return ans
    else:
        tmp = set()
        for a in ans:
            for s in ['a','b','c']:
                tmp.add(a+s)
        # print(tmp)
        return saiki(tmp,i-1) 

def main():
    N = int(input())
    ans = saiki({'a','b','c'},N)
    [print(a) for a in sorted(ans)]


if __name__ == "__main__":
    main()
