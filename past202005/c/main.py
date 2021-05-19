#!/usr/bin/env python3


def main():
    A, R, N = map(int, input().split())
    ans =  A
    if R == 1:
        print(A)
        exit()
    for i in range(N-1):
        ans *= R
        if ans > 10**9:
            print('large')
            exit()
    print(ans)

if __name__ == "__main__":
    main()
