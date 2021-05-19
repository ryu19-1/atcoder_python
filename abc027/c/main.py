#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
import math

def main():
    N = int(input())
    depth = math.floor(math.log2(N))
    now = 1
    ans = 0
    while now <= N:
        if ans % 2 != depth % 2:# Tの番
            now *= 2
        else:
            now = now * 2 + 1
        ans += 1
    print(['Takahashi','Aoki'][ans % 2])


if __name__ == "__main__":
    main()
