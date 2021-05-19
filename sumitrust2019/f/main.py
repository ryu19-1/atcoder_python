#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())
    A1 -= B1
    A2 -= B2
    if A1 < 0:
        A1 = -A1
        A2 = -A2
    # print(A1*T1 + A2*T2)
    if A1 * T1 + A2 * T2 > 0:
        print(0)
    elif A1 * T1 + A2 * T2 == 0:
        print('infinity')
    else:
        now = A1*T1
        diff = abs(A1*T1+A2*T2)
        ans = 1 + 2*(now // diff)
        if now % diff == 0:
            ans -= 1
        print(ans)


if __name__ == "__main__":
    main()
