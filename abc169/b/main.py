#!/usr/bin/env python3


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 1
    for i in range(N):
        ans *= A[i]
        if ans > 10**18:
            print(-1)
            exit()
    print(ans)

if __name__ == "__main__":
    main()
