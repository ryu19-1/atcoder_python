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
    N, A, B = map(int, input().split())
    v = list(map(int, input().split()))
    cnt = defaultdict(int)

    for i in range(N):
        cnt[v[i]] += 1
    v.sort(reverse=True)
    maxi = -1
    maxave = -1
    ans = []
    for i in range(A, B + 1):
        vv = [sum(v[:i]), i]
        pattern = 1
        for key, value in Counter(v[:i]).items():
            for z in range(value):
                pattern *= (cnt[key] - z)
                pattern //= z+1
            # pattern *= (a[cnt[key]] * inva[value] %
            #             p) * inva[cnt[key] - value] % p
        ans.append([vv, pattern])
    # print(ans)
    maxvv = [0, 1]
    piyo = 0
    for vv, pattern in ans:
        if maxvv[0] * vv[1] < maxvv[1] * vv[0]:
            maxvv = vv[:]
            piyo = pattern
        elif maxvv[0] * vv[1] == maxvv[1] * vv[0]:
            piyo += pattern
    print(maxvv[0]/maxvv[1])
    print(piyo)


if __name__ == "__main__":
    main()
