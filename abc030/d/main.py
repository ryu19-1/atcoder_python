#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    N, a = map(int, input().split())
    a -= 1
    k = int(input())
    b = list(map(lambda x: int(x)-1, input().split()))
    now = b[a]
    checked = set()
    root = [a]
    checked.add(a)
    while now not in checked:
        checked.add(now)
        root.append(now)
        now = b[now]
    # print(root, now)
    if k < len(root):
        print(root[k]+1)
    else:
        k -= len(root)
        k %= len(root) - root.index(now)
        # print(k)
        print(root[root.index(now):][k]+1)


if __name__ == "__main__":
    main()
