#!/usr/bin/env python3


def main():
    N = int(input())
    a = [set(list(input())) for _ in range(N)]
    ans = ''
    if N == 1:
        print(a[0].pop())
        exit()
    for i in range(N//2):
        tmp = a[i] & a[N-1-i]
        if len(tmp) == 0:
            exit(print(-1))
        else:
            ans += tmp.pop()
    if N % 2 == 0:
        print(ans+ans[::-1])
    else:
        print(ans+a[N//2].pop()+ans[::-1])

if __name__ == "__main__":
    main()
