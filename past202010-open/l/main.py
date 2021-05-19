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
    N, Q = map(int, input().split())
    h = list(map(int, input().split()))
    even_dict = defaultdict(int)
    odd_dict = defaultdict(int)
    for i in range(N - 1):
        if i % 2 == 0:
            odd_dict[h[i + 1] - h[i]] += 1
        else:
            even_dict[h[i + 1] - h[i]] += 1

    X = 0  # 奇数、偶数で変動

    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            X += query[1]
        elif query[0] == 2:
            X -= query[1]
        else:
            u = query[1]-1
            v = query[2]
            if u % 2 == 0:  # 奇数マンションがv増える
                if u > 0:
                    even_dict[h[u] - h[u-1]] -= 1
                    even_dict[h[u] - h[u-1] + v] += 1
                if u < N - 1:
                    odd_dict[h[u+1] - h[u]] -= 1
                    odd_dict[h[u+1] - h[u] - v] += 1
            else:
                if u > 0:
                    odd_dict[h[u] - h[u-1]] -= 1
                    odd_dict[h[u] - h[u-1] + v] += 1
                if u < N - 1:
                    even_dict[h[u+1] - h[u]] -= 1
                    even_dict[h[u + 1] - h[u] - v] += 1
            h[u] += v
        ans = even_dict[-X] + odd_dict[X]
        print(ans)


if __name__ == "__main__":
    main()
