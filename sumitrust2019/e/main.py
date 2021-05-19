#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    A = list(map(int, input().split()))
    p = 10**9+7
    # check[i]:= Aの中のiが出てきた順番
    check = [[] for _ in range(N)]
    for i in range(N):
        check[A[i]].append(i)
    
    # print(check)
    ans = 1
    for i in range(len(check[0])):
        ans *= (3-i)

    for i in range(1,N):
        if len(check[i-1]) < len(check[i]):
            exit(print(0))
        # check[i]がcheck[i-1]のなかで何番目か調べる
        for j in range(len(check[i])):
            d = bisect_right(check[i-1],check[i][j])
            if d < j:
                exit(print(0))
            ans *= d-j
            ans %= p
            # print(ans)
    print(ans)

if __name__ == "__main__":
    main()
