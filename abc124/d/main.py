#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

def main():
    N, K = map(int, input().split())
    S = input()
    nums = []
    # 1の個数、0の個数を交互に記録していく
    if S[0] == '0': nums.append(0)
    i = 0
    while i < N:
        j = i
        while j < N and S[i]==S[j]:
            j += 1
        nums.append(j-i)
        i = j
    if S[-1] == '0': nums.append(0)
    # print(nums)
    nums = [0] + list(accumulate(nums))
    # print(nums)
    ans = 0
    
    for i in range(0,len(nums),2):
        # print(i)
        ans = max(ans,nums[min(i+2*K+1,len(nums)-1)]-nums[i])
    print(ans)
        

if __name__ == "__main__":
    main()
