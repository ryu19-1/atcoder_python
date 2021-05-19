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
    B, C = map(int, input().split())
    ans = 1
    if B <= 0:
        ans += C // 2
        ans += (C - 1) // 2
        if B < 0:
            ans += 1
            if 2*abs(B) <= C-1:
                ans += max(0, 2 * abs(B) - 1)
            else:
                ans += (C-1)//2 + max(0, (C-2)//2)
    else:
        ans += (C - 1) // 2 + 1
        ans += max(0, (C - 2) // 2)
        if 2*B <= C:
            ans += 2 * B - 1
        else:
            ans += C//2 + (C-1)//2
    print(ans)


if __name__ == "__main__":
    main()
