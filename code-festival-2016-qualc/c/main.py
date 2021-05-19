#!/usr/bin/env python3

def main():
    N = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))

    if T[-1] != A[0]:
        print(0)
        exit()

    upper = T[:]
    flag = [0] * N

    # Tくんの目線で見る
    now = 0
    for i in range(N):
        if T[i] > now:
            flag[i] = 1
            now = T[i]

    # A君の目線で見る
    now = 0
    for i in range(N):
        if flag[N-1-i] and T[N-1-i] > A[N-1-i]:
            print(0)
            exit()

        if A[N-1-i] > now:
            flag[N-1-i] = 1
            now = A[N-1-i]

        upper[N-1-i] = min(upper[N-1-i],A[N-1-i])

    ans = 1
    m = 10**9+7
    for i in range(N):
        if flag[i]==0:
            ans *= upper[i]
            ans %= m
    print(ans)

if __name__ == "__main__":
    main()