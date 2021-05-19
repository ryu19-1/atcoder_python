#!/usr/bin/env python3


def main():
    N, M = map(int, input().split())
    if M < 2*N:  # ありえない
        print(-1, -1, -1)
    elif M <= 3*N:
        print(3*N-M, M-2*N, 0)
    elif M <= 4*N:
        print(0,4*N-M,M-3*N)
    else:
        print(-1, -1, -1)


if __name__ == "__main__":
    main()
