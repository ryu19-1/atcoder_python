#!/usr/bin/env python3
# import sys
# from collections import deque, Counter
# from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate


def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    W = list(map(int, input().split()))
    ans = 10 ** 18
    diff = [0] * (N - 1)
    for i in range(N-1):
        diff[i] = H[i + 1] - H[i]
    # print(diff)
    evendiff = [0] + list(accumulate(diff[::2]))
    odddiff = [0] + list(accumulate(diff[1::2]))
    # print(evendiff, odddiff)

    for i in range(M):
        d = bisect_right(H, W[i])
        # print(i, d, W[i])
        res = 0
        if d > 0:
            # res += sum(diff[0:d - 1:2])
            res += evendiff[d//2]
        # print(res, diff[0:d-1:2])
        if d % 2 == 0:
            res += H[d] - W[i]
        else:
            res += W[i] - H[d - 1]
        # print(res)
        # res += sum(diff[(d // 2) * 2 + 1::2])
        res += odddiff[-1] - odddiff[d // 2]
        # print((odddiff[-1] - odddiff[d // 2]))
        # print(diff[(d // 2) * 2 + 1::2], d)
        # print(res)

        ans = min(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
