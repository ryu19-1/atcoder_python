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
    T = int(input())
    for _ in range(T):
        ax, ay, bx, by, cx, cy = map(int, input().split())
        minx = min([ax, bx, cx])
        miny = min([ay, by, cy])
        # print(minx, miny)

        # 完成位置の石の向きを調べる
        ax -= minx
        bx -= minx
        cx -= minx
        ay -= miny
        by -= miny
        cy -= miny
        d = {(0, 0), (0, 1), (1, 0), (1, 1)}  # 石がない場所
        d -= {(ax, ay)}
        d -= {(bx, by)}
        d -= {(cx, cy)}
        d = list(d)
        z = d[0][0] + d[0][1]*2
        s = 3  # 初期位置の石の向き
        # print(z)

        # 石の位置を第一象限に写す
        if minx >= 0 and miny < 0:
            miny = -miny
            z = [2, 3, 0, 1][z]
            s = 3
            miny -= 1
        elif minx < 0 and miny >= 0:
            minx = -minx
            z = [1, 0, 3, 2][z]
            s = 0
            minx -= 1
        elif minx < 0 and miny < 0:
            minx = -minx
            miny = -miny
            z = [3, 2, 1, 0][z]
            s = 2
            minx -= 1
            miny -= 1

        print(minx, miny, z, s)

        ans = 0
        if minx == 0 and miny == 0:
            if z != s:
                ans += 1
        else:
            if z != 3:
                ans += 1
            if s == 0:
                ans -= 1
            elif s == 1 and miny > 0:
                ans -= 1
            elif s == 2 and minx > 0:
                ans -= 1
            ans += 3 * min(minx, miny)
            minx -= min(minx, miny)
            miny -= min(minx, miny)
            ans += 2 * max(0, minx-1)
            ans += 2 * max(0, miny-1)

        print(ans)


if __name__ == "__main__":
    main()
