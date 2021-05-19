#!/usr/bin/env python3
from collections import Counter
import math

def make_prime_list(N):
    prime_list = [2]
    for i in range(3,int(N**0.5)+1,2):
        flag = True
        for j in range(3,int(i**0.5)+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            prime_list.append(i)
    return prime_list

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    N = int(input())
    C = Counter(prime_factorize(N))
    # print(C)
    ans = 0
    for c in C.values():
        tmp = c
        i = 1
        while tmp >= i:
            tmp -= i
            ans += 1
            i += 1
    print(ans)


if __name__ == "__main__":
    main()