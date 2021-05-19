#!/usr/bin/env python3
import math

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f**2 <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    A, B = map(int, input().split())
    C = math.gcd(A,B)
    if C == 1:
        print(1)
    else:
        ans = prime_factorize(C)
        print(len(set(ans)) + 1)


if __name__ == "__main__":
    main()
