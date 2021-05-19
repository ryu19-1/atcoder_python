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
    s = input()
    ans = N
    d = deque()
    for i in range(N):
        d.append(s[i])
        if len(d) > 2:
            s1 = d.pop()
            s2 = d.pop()
            s3 = d.pop()
            if s1 == 'x' and s2 == 'o' and s3 == 'f':
                ans -= 3
            else:
                d.append(s3)
                d.append(s2)
                d.append(s1)
    print(ans)


if __name__ == "__main__":
    main()
