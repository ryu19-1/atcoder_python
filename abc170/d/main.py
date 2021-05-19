#!/usr/bin/env python3
from collections import Counter
from itertools import accumulate

def main():
    N = int(input())
    A = sorted(map(int, input().split()))

    print(A)

    # 倍数リストを保持して、チェックしていく
    B = [0] * (A[N-1]+1)
    for i in range(N):
        j = A[i]
        while j <= A[N-1]:
            B[j] += 1
            j += A[i]
    print(B)
    ans = 0
    for i in range(N):
        if B[A[i]] == 1:
            ans += 1
    print(ans)

    # A = [1,2,3,4,...10**6]
    # 10**6*18


if __name__ == "__main__":
    main()
