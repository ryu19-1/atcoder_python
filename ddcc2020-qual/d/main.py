#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    M = int(input())
    # d = [None]*M
    # c = [None]*M
    sumc = 0
    sumd = 0
    for i in range(M):
        td, tc = map(int, input().split())
        # d[i] = td
        # c[i] = tc
        sumc += tc
        sumd += td*tc
    # result = sumd%10+sumd//10
    # # print(sumd,c,d,result)
    # if result > 9:
    #     print(sum(c)+sumd//10)
    # else:
    print(sumc-1+(sumd-1)//9)

if __name__ == "__main__":
    main()
