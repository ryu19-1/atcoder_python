#!/usr/bin/env python3


def main():
    A, B = map(int, input().split())
    arr = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2]
    res = abs(A - B)
    print(res//10 + arr[res % 10])


if __name__ == "__main__":
    main()
