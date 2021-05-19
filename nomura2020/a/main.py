#!/usr/bin/env python3


def main():
    H1, M1, H2, M2, K = map(int, input().split())
    print(60*(H2-H1) + (M2-M1)-K)

if __name__ == "__main__":
    main()
