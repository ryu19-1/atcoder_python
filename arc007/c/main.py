#!/usr/bin/env python3


def main():
    c = input()
    N = len(c)
    ans = N
    for i in range(1 << N):
        check = [0] * N
        cnt = 0
        for j in range(N):
            if i & (1 << j):
                cnt += 1
                for k in range(N):
                    check[(j + k) % N] += int(c[k] == 'o')
        if check.count(0) == 0:
            ans = min(ans, cnt)
    print(ans)


if __name__ == "__main__":
    main()
