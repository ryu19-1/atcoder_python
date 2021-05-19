#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, M = map(int, input().split())
    AB = [[] for _ in range(10**5)]
    for i in range(N):
        a, b = map(int, input().split())
        AB[a-1].append(b)
    
    q = []
    ans = 0
    i = 0
    while i < M:
        for ab in AB[i]:
            heappush(q,-ab)
        if q:
            ans -= heappop(q)
        i += 1
    print(ans)


if __name__ == "__main__":
    main()
