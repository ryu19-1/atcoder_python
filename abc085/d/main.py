#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right,bisect_left
from itertools import accumulate

def main():
    N, H = map(int, input().split())
    a = [None] * N
    b = [None] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    i = bisect_left(b,a[N-1])
    c = list(accumulate(b[i:][::-1]))
    # print(c)
    M = len(c)
    count = bisect_left(c,H)
    if count < M:
        print(count+1)
    else:
        print(count + (H-c[M-1] + a[N-1]-1)//a[N-1])

if __name__ == "__main__":
    main()
