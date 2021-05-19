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
    A, B = map(int, input().split())
    ans = A-B
    for i in range(6):
        for j in range(10):  # 0-9
            if i == 0 and j == 0:
                continue
            if i == 3 and j == 0:
                continue
            tmpA = str(A)
            tmpB = str(B)
            if i < 3:
                if int(tmpA[i]) == j:
                    continue
                tmpA = tmpA[:i]+str(j)+tmpA[i+1:]
            else:
                if int(tmpB[i-3]) == j:
                    continue
                tmpB = tmpB[:i-3]+str(j)+tmpB[i-2:]
            # print(tmpA, tmpB)
            ans = max(ans, int(tmpA) - int(tmpB))
    print(ans)


if __name__ == "__main__":
    main()
