#!/usr/bin/env python3


def main():
    txa, tya, txb, tyb, T, V = map(int, input().split())
    n = int(input())
    girls = [None] * n
    for i in range(n):
        girls[i] = list(map(int, input().split()))

    for i in range(n):
        dist = (abs(txa-girls[i][0])**2 + abs(tya-girls[i][1])**2) ** 0.5
        dist += (abs(txb-girls[i][0])**2 + abs(tyb-girls[i][1])**2) ** 0.5
        if dist <= T*V:
            print('YES')
            exit()
    print('NO')

if __name__ == "__main__":
    main()
