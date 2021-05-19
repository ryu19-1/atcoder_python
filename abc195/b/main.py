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
    A, B, W = map(int, input().split())
    W *= 1000
    ans = [INF, -1]
    count = 1
    while count * A <= W:
        if count*A <= W <= count*B:
            ans[0] = min(ans[0], count)
            ans[1] = max(ans[1], count)
        count += 1
    # print(ans)
    if ans == [INF, -1]:
        print('UNSATISFIABLE')
    else:
        print(*ans)


if __name__ == "__main__":
    main()
