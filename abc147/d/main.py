#!/usr/bin/env python3


def main():
    N = int(input())
    A = list(map(int, input().split()))
    p = 10**9 + 7

    digit_0 = [0] * 60
    digit_1 = [0] * 60

    for i in range(N):
        for j in range(60):
            if (A[i] >> j) & 1:
                digit_1[j] += 1
            else:
                digit_0[j] += 1
    
    ans = 0
    for j in range(60):
        ans += ((digit_0[j] * digit_1[j] % p) * pow(2,j,p) % p)
        ans %= p
    print(ans)

if __name__ == "__main__":
    main()
