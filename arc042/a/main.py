#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, M = map(int, input().split())
    ans = [[i+1+M,i+1] for i in range(N)]
    for j in range(M):
        a = int(input())
        ans[a-1][0] = M - j
    ans.sort()
    for i in range(N):
        print(ans[i][1])

if __name__ == "__main__":
    main()
