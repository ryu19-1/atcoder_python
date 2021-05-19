#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush


def main():
    N = int(input())
    if N == 1:
        print(0)
        exit()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p = list(map(lambda x: int(x)-1, input().split()))
    q = []
    reverse = [None] * N
    for i in range(N):
        if i != p[i] and a[i] <= b[p[i]]:
            print(-1)
            exit()
        else:
            reverse[p[i]] = i
    q = []
    for i in range(N):
        heappush(q, (a[i], i))

    ans = []
    while q:
        limit, i = heappop(q)
        if i == reverse[i]:
            continue
        ans.append((i, reverse[i]))
        reverse[p[i]] = reverse[i]
        p[reverse[i]] = p[i]
        reverse[i] = -1
        p[i] = -1
        # print(i, reverse, p)
    print(len(ans))
    for a in ans:
        print(a[0]+1, a[1]+1)


if __name__ == "__main__":
    main()
