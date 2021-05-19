#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    ans = [0,0,0,0]
    for _ in range(N):
        s = input()
        if s == 'AC':
            ans[0] += 1
        elif s == 'WA':
            ans [1] += 1
        elif s == 'TLE':
            ans[2] += 1
        else:
            ans[3] += 1
    print('AC x '+str(ans[0]))
    print('WA x '+str(ans[1]))
    print('TLE x '+str(ans[2]))
    print('RE x '+str(ans[3]))


if __name__ == "__main__":
    main()
