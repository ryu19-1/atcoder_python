#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    K = int(input())
    A = list(map(int, input().split()))
    if A[-1]!= 2:
        print(-1)
        exit()
    ans = 2
    for i in range(K):
        a = A[K-1-i]
        if ans*2 <= a:
            print(-1)
            exit()
        elif ans <= a:
            ans = a
        else:
            t = (ans+a-1)//a
            ans = t * a
        # print(ans)
    print(ans, ans+a-1)

if __name__ == "__main__":
    main()
