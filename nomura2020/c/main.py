#!/usr/bin/env python3
from itertools import accumulate

def main():
    N = int(input())
    A = list(map(int, input().split()))
    accumA = list(accumulate(A[::-1]))[::-1]
    ans = 1
    ne = [0] * (N+1)
    ne[0] = 1

    if A[0] != 0:
        if A[0] == 1 and N == 0:
            print(1)
            exit()
        else:
            print(-1)
            exit()


    for i in range(1,N+1):
        if i == N:# 最後の深さ
            if ne[i-1] > A[i] or ne[i-1] * 2 < A[i]:
                print(-1)
                exit()
            else:
                ans += A[i]
        else:
            tmp_ne = min(ne[i-1]*2 - A[i], accumA[i+1])
            if tmp_ne < 0:
                print(-1)
                exit()
            else:
                ne[i] = tmp_ne
                ans += tmp_ne + A[i]
    print(ans)
    # print(ne,accumA)


if __name__ == "__main__":
    main()
