#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left

def main():
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    time = 0
    c = [a,b]
    d = [X,Y]
    K = [N,M]
    while True:
        i = bisect_left(c[ans % 2],time)
        if i == K[ans % 2]:
            break
        else:
            time = c[ans % 2][i] + d[ans % 2]
            ans += 1
    print(ans//2)

if __name__ == "__main__":
    main()
