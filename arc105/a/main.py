#!/usr/bin/env python3


def main():
    A = list(map(int, input().split()))
    sumA = sum(A)
    for i in range(2 ** 4):
        tmp = 0
        for j in range(4):
            if i >> j & 1:
                tmp += A[j]
        if tmp == sumA-tmp:
            # print(tmp)
            print('Yes')
            exit()
    print('No')


if __name__ == "__main__":
    main()
