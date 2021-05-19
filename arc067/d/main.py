#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))

    ans = 0
    for i in range(N-1):
        tmp = A * (X[i+1]-X[i])
        ans += min(tmp,B)
    print(ans)

if __name__ == "__main__":
    main()
