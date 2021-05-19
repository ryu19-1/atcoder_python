#!/usr/bin/env python3


def main():
    N = int(input()) % 30
    ans = list('123456')
    for i in range(N):
        ans[i%5], ans[i%5+1] = ans[i%5+1], ans[i%5]
    print(''.join(ans))

if __name__ == "__main__":
    main()
