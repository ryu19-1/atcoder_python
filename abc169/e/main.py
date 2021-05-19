#!/usr/bin/env python3


def main():
    N = int(input())
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    if N % 2 == 1:
        print(B[(N-1)//2] - A[(N-1)//2] + 1)
    else:
        print(B[N//2]-A[N//2] +B[N//2-1]-A[N//2-1] + 1)
    

if __name__ == "__main__":
    main()
