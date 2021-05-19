#!/usr/bin/env python3


def main():
    N, L = map(int, input().split())
    a = list(map(int, input().split()))
    flag = False
    ans = []
    for i in range(N - 1):
        if a[i] + a[i + 1] >= L:
            flag = True
            ans.append(i + 1)
            break
    if flag:
        print('Possible')
        ans = [*range(1, ans[-1])] + [*range(ans[-1] + 1, N)][::-1] + ans
        for a in ans:
            print(a)
    else:
        print('Impossible')


if __name__ == "__main__":
    main()
