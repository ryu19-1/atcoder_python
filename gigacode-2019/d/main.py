#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    H, W, K, V = map(int, input().split())
    A = [None for _ in range(H)]
    for i in range(H):
        A[i] = list(map(int, input().split()))

    #Aの2次元累積和
    S = [[0]*(W+1) for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            S[i+1][j+1] = S[i][j+1]+S[i+1][j]-S[i][j]+A[i][j]
    # print(S)
    ans = 0

    for i in range(1,H+1):
        for j in range(1,W+1):
            for k in range(i,H+1):
                for l in range(j,W+1):
                    tmpS = (k-i+1)*(l-j+1)
                    tmp = S[k][l]-S[i-1][l]-S[k][j-1]+S[i-1][j-1]
                    if tmp+tmpS*K <= V:
                        ans = max(ans,tmpS)
    print(ans)

if __name__ == "__main__":
    main()
