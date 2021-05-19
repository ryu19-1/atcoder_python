#!/usr/bin/env python3


def main():
    N = int(input())
    if N == 0:
        print(0)
        exit()

    ans = ''
    while N != 1:
        m = N % (-2)
        ans += str(abs(m))
        N = N // (-2)
        if m != 0:
            N += 1
        # print(ans,N)
    ans += str(N)
    print(ans[::-1])

if __name__ == "__main__":
    main()
