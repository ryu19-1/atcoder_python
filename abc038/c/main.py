#!/usr/bin/env python3


def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    i = 0
    tmp = 1
    while i < N:
        if i < N-1 and a[i] < a[i+1]:
            tmp += 1
        else:
            ans += tmp * (tmp+1) // 2
            # print(tmp,ans)
            tmp = 1
        i += 1
    print(ans)


if __name__ == "__main__":
    main()
