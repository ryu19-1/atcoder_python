#!/usr/bin/env python3


def main():
    K = int(input())
    S = input()
    N = len(S)
    if N <= K:
        print(S)
    else:
        print(S[:K]+'...')

if __name__ == "__main__":
    main()
