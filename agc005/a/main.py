#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    X = input()
    ans = 0
    now = 0
    for x in X:
        if x == 'S':
            now -= 1
        else:
            now += 1
        ans = max(ans,now)
    print(ans*2)

if __name__ == "__main__":
    main()
