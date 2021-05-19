#!/usr/bin/env python3


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = sum(A)
    for i in range(0,N-1,2):
        # print(i)
        tmp = ans - 2*(A[i]+A[i+1])
        if tmp > ans:
            ans = tmp
    print(ans)

if __name__ == "__main__":
    main()
