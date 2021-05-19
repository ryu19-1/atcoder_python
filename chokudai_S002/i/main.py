#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
from math import gcd

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    lcm = AB[0][1]
    for i in range(1, N):
        lcm = (lcm * AB[i][1]) // gcd(lcm, AB[i][1])
    ans = -1
    now = -1
    ans = [AB[i][0] * lcm * AB[i][1] for i in range(N)]
    print(ans)
    if ans.count(max(ans)) > 1:
        print(-1)
    else:
        print(ans.index(max(ans)))


if __name__ == "__main__":
    main()
