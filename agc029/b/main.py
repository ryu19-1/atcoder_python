#!/usr/bin/env python3
import sys
from collections import deque, Counter, defaultdict
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    two = [2]
    while two[-1] <= 10 ** 9:
        two.append(two[-1] * 2)
    ans = 0
    dic = defaultdict(int)
    dic[a[N - 1]] += 1
    for i in range(N - 2, -1, -1):
        flag = False
        for t in two[::-1]:
            if t - a[i] <= 0:
                break
            if dic[t - a[i]] > 0:
                flag = True
                dic[t - a[i]] -= 1
                ans += 1
                break
        if flag:
            pass
        else:
            dic[a[i]] += 1
    print(ans)


if __name__ == "__main__":
    main()
