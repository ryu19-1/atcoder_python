#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0# 初期幸福な人数
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    M = []# 'RL'の位置を格納
    if S[0] == 'L':
        M.append(1)
        # ans -= 1
    for i in range(1,N-1):
        if S[i:i+2] == 'RL':
            M.append(2)
            # ans -= 2
    if S[N-1] == 'R':
        M.append(1)
        # ans -= 2
    M.sort(reverse=True)
    # print(M,ans)
    print(min(N-1,ans + sum(M[:K])))
    

if __name__ == "__main__":
    main()
