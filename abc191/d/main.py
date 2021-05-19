#!/usr/bin/env python3
from decimal import Decimal

INF = 10**24


def kiri(n):
    if n >= 0:
        return (n // 10000) * 10000
    else:
        return -(n//(-10000))*10000


def main():
    X, Y, R = input().split()
    X = int(Decimal(X) * Decimal('10000'))
    Y = int(Decimal(Y) * Decimal('10000'))
    R = int(Decimal(R) * Decimal('10000'))
    start = kiri(Y - R)
    end = kiri(Y + R)
    ans = 0
    for now in range(start, end + 1, 10000):
        T = R * R - (now - Y) * (now - Y)
        if T < 0:
            continue
        # (x-a)^2 = Tなるxの左端を調べる
        tmpL = kiri(int(X - T ** 0.5))
        l = -INF
        for tmp in range(tmpL - 50000, tmpL + 50001, 10000):
            if (tmp - X) ** 2 <= T:
                l = tmp
                break

        tmpR = kiri(int(X + T ** 0.5))
        r = INF
        for tmp in range(tmpR + 50000, tmpR - 50001, -10000):
            if (tmp - X) ** 2 <= T:
                r = tmp
                break
        if l <= r and l != -INF and r != INF:
            ans += (r-l)//10000 + 1
    print(ans)


if __name__ == "__main__":
    main()
