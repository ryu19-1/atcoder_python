#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sumA = sum(A)//2
    B = A 
    odd = list(accumulate([0] + B[::2]+ B[1::2]))# 0+1, 2+3,...
    even = list(accumulate([0] + B[1::2]+ B[0::2]))# 1+2, 3+4,...

    # ans = [None] * N
    # for i in range(N):
    #     if i % 2 == 0:# evenから引く
    #         # print(even[N//2+i//2],even[i//2])
    #         ans[i] = 2*(sumA-(even[N//2+i//2]-even[i//2]))
    #     else:
    #         ans[i] = 2*(sumA-(odd[N//2+(i+1)//2]-odd[(i+1)//2]))
    # print(*ans)

    ## 別解 ##
    ans = [None] * N
    ans[0] = 2*(sumA - sum(A[1::2]))
    for i in range(N-1):
        ans[i+1] = 2*A[i] - ans[i]
    print(*ans)

if __name__ == "__main__":
    main()
