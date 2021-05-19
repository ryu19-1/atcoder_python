#!/usr/bin/env python3


def main():
    N = int(input())
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    
    p = 10**9 + 7
    ans = pow(2, N, p)
    
    

if __name__ == "__main__":
    main()
