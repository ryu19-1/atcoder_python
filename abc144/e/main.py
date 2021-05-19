#!/usr/bin/env python3


N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)


def check(x):
    # N人全員の間食までにかかる時間をx以下に抑えられるか判定
    rem = K
    for i in range(N):
        if A[i] * F[i] <= x:
            continue
        else:
            r = (A[i] * F[i] - x + F[i] - 1) // F[i]
            rem -= r
            if rem < 0:
                return False
    return True


def main():
    # 答えの値で二分探索
    l = -1
    r = 10 ** 19
    while (r - l > 1):
        mid = (r + l) // 2
        if check(mid):
            r = mid
        else:
            l = mid
    print(r)


if __name__ == "__main__":
    main()
