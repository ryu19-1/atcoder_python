#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    H, W = map(int, input().split())
    N = int(input())
    a = list(map(int, input().split()))
    ans = [[None]*W for _ in range(H)]
    now = 0
    for i in range(N):
        while a[i] > 0:
            # print(now//W, now%W)
            ans[now//W][now%W]=(i+1)
            now += 1
            a[i] -= 1
    for i in range(H):
        if i % 2 == 1:
            print(*ans[i][::-1])
        else:
            print(*ans[i])

if __name__ == "__main__":
    main()
