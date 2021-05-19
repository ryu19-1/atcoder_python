#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    s = input()
    N = len(s)
    l = 0
    r = N-1
    ans = 0
    while s[l:r+1]:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] == 'x':
            ans += 1
            l += 1
        elif s[r] == 'x':
            ans += 1
            r -= 1
        else:
            print(-1)
            exit()
    print(ans)




if __name__ == "__main__":
    main()
