#!/usr/bin/env python3
import math

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - i - 1 for i in range(N)]
    A.sort()
    diff = A[(N-1)//2]
    print(sum([abs(a-diff) for a in A]))

if __name__ == "__main__":
    main()
