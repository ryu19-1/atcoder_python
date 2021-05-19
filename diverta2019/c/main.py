#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    s = [input() for _ in range(N)]
    a = 0
    b = 0
    c = 0#a&b
    ans = 0
    for i in range(N):
        if s[i][0] == 'B':
            if s[i][-1] == 'A':
                c += 1
            else:
                b += 1
        elif s[i][-1] == 'A':
            a += 1
        ans += s[i].count('AB')
      
    if a+b>0:
        print(ans + (c-1) + min(a+1,b+1))
    else:
        print(ans + max(0,c-1))
    
    x = -3
    y = 2
    print(x//y)
    print(-(x//(-y)))

if __name__ == "__main__":
    main()
