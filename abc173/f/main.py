#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += N * (N + 1) // 2
        if i > 1:
            ans -= (i - 1) * i // 2
        if i < N:
            ans -= (N - i + 1) * (N - i) // 2
        # print(i, ans)

    for i in range(N - 1):
        u, v = map(int, input().split())
        if v < u:
            u, v = v, u
        ans -= u*(N-v+1)
    print(ans)


if __name__ == "__main__":
    main()
