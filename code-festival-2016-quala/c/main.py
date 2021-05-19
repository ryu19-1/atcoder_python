#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    s = list(input())
    N = len(s)
    K = int(input())
    i = 0
    while K > 0:
        if i == N-1:
            num = ord(s[i])+K%26
            if num > ord('z'):
                num -= 26
            s[i] = chr(num)
            break
        else:
            if s[i] != 'a':
                num = 26-ord(s[i])+ord('a')
                if  num <= K:
                    s[i] = 'a'
                    K -= num
            i += 1
    print(''.join(s))

if __name__ == "__main__":
    main()
