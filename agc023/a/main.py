#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right,bisect_left
from itertools import accumulate

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # B = sorted(accumulate(A))
    A = [0] + list(accumulate(A))
    ans = 0
    # print(B,A)
    for l in Counter(A).values():
        # print(l)
        ans += l*(l-1)//2
    print(ans)


if __name__ == "__main__":
    main()
