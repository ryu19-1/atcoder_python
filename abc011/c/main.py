#!/usr/bin/env python3


def main():
    N = int(input())
    NGs = [int(input()) for _ in range(3)]
    if N in NGs:
        print('NO')
        exit()
    ans = 0
    now = N
    while ans < 100:
        if now <= 3:
            ans += 1
            print('YES')
            exit()
        if now-3 in NGs:
            if now-2 in NGs:
                if now-1 in NGs:
                    print('NO')
                    exit()
                else:
                    now -= 1
            else:
                now -= 2
        else:
            now -= 3
        ans += 1
    print('NO')

if __name__ == "__main__":
    main()
