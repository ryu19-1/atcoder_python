#!/usr/bin/env python3


def main():
    N, M = map(int, input().split())
    if N == 1 and M == 0:
        print(1, 2)
    if abs(M) == N or M < 0:
        print(-1)
        exit()
    if M == 0:
        for i in range(N):
            print(1 + 2*i, 1 + 2*i+1)  # [Li, Ri]
    else:
        # 高橋君はM-1を出力すれば良い
        for i in range(M+1):
            print(10**7 + 2*i, 10**7 + 2*i+1)
        for i in range(N-M-1):
            print(1 + i, 10 ** 9 - i)  # これで青木君の値は1に固定


if __name__ == "__main__":
    main()
