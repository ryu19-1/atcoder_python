#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate


def main():
    n = int(input())
    ans = [0]*(10**6+2)
    for i in range(n):
        a, b = map(int, input().split())
        ans[a] += 1
        ans[b+1] -= 1
    ans = list(accumulate(ans))
    print(max(ans))

if __name__ == "__main__":
    main()
