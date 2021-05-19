#!/usr/bin/env python3


def main():
    x, y, z = map(int, input().split())
    p = 10**9 + 7
    ans = z
    while 1:
        if ans % 17 == x and ans % 107 == y:
            print(ans)
            break
        else:
            ans += p

if __name__ == "__main__":
    main()
