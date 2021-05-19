#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

def main():
    s = input()
    N = len(s)
    # 方針: アルファベット各文字の前回出現位置を記録
    nums = [-1] * 26
    for i in range(N):
        x = ord(s[i]) - ord('a')
        if nums[x] == -1:
            nums[x] = i
        else:
            # 差が2以下ならダメ
            if i - nums[x] < 3:
                print(nums[x]+1, i+1)
                exit()
            else:
                nums[x] = i
    print(-1,-1) 

if __name__ == "__main__":
    main()