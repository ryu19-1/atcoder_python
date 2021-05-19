#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 2 for _ in range(30)]
    ans = 0
    for j in range(N):
        if K & AB[j][0] == AB[j][0]:
            ans += AB[j][1]
    mask = K
    for i in range(30):
        if (1 << i) & K:  # 1が立っている時
            # print(mask)
            res = 0
            for j in range(N):
                if (mask-1) & AB[j][0] == AB[j][0]:
                    res += AB[j][1]
            ans = max(ans, res)
            mask -= 1 << i
    print(ans)


if __name__ == "__main__":
    main()
