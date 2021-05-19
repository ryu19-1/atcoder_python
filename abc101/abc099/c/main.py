#!/usr/bin/env python3
import math
# n進数の各位の和


def base_10_n(x, n):
    if x == 0:
        return 0
    # logで桁数出してはいけない、浮動小数点の誤差があるから死ぬ
    a = int(math.log(x, n))
    ans = 0
    for i in range(a, -1, -1):
        ans += x // n**i
        x %= n**i
    ans += x
    return ans


def s(n, r):
    if n == 0:
        return 0
    return n % r + s(n // r, r)


def main():
    # N = int(input())
    # ans = 10**12
    # for j in range(N+1):
    #     # c = base_10_n(N-j, 6)
    #     # d = base_10_n(j, 9)
    #     c = s(j,6)
    #     d = s(N-j,9)
    #     ans = min(ans, c+d)
    # print(ans)
    for i in range(1,10**5):
        if base_10_n(i,9) != s(i,9):
            print(i,base_10_n(i,9),s(i,9))
            print(math.log(9**5,9))


if __name__ == "__main__":
    main()
