#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    A = list(map(int, input().split()))
    l = Counter(A)
    # print(l)
    Q = int(input())
    ans = sum(A)
    
    for i in range(Q):
        B, C = map(int, input().split())
        tmp = l[B]
        l[C]+=tmp
        l[B] = 0
        ans += (C-B)*tmp
        print(ans)


if __name__ == "__main__":
    main()
