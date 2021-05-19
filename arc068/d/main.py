#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    A = list(map(int, input().split()))
    l = Counter(A)
    ans = N - sum(l.values()) + len(l)
    if ans % 2 == 0: ans -= 1
    print(ans)

if __name__ == "__main__":
    main()
