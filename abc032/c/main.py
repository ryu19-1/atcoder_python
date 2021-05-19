#!/usr/bin/env python3


def main():
    N, K = map(int, input().split())
    s = [int(input()) for _ in range(N)]
    if 0 in s:
        exit(print(N))
    ans = 0
    l = 0
    r = 0
    mul = 1
    while r < N:
        mul *= s[r]
        if mul > K:
            ans = max(ans, r-l)
            mul /= s[l]
            l += 1
        if r == N-1 and mul <= K:
            ans = max(ans, r-l+1)
        r += 1
        # print(l,r)
    print(ans)


if __name__ == "__main__":
    main()
