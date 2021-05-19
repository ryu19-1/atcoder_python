#!/usr/bin/env python3


def main():
    N = int(input())
    X = [None] * N
    for i in range(N):
        x, l = map(int, input().split())
        X[i] = (x+l,x-l)
    X.sort()
    ans = 0
    maxT = - 10**18
    for i in range(N):
        if maxT <= X[i][1]:
            ans += 1
            maxT = X[i][0]
    print(ans) 


if __name__ == "__main__":
    main()
