#!/usr/bin/env python3


def main():
    N = int(input())
    for i in range(1, 50):
        for j in range(1, 50):
            if pow(3, i) + pow(5, j) == N:
                print(i, j)
                exit()
    print(-1)


if __name__ == "__main__":
    main()
