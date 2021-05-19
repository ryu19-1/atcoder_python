#!/usr/bin/env python3


def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    ans = 10**9
    for i in range(4**N):
        # N本の竹がA,B,Cのどれに使われるか
        cost = [[] for _ in range(3)]
        tmp = i
        j = 0
        while j < N:
            if tmp % 4 < 3:
                cost[tmp % 4].append(l[j])
            j += 1
            tmp //= 4

        if len(cost[0]) == 0 or len(cost[1]) == 0 or len(cost[2]) == 0:
            continue

        tmpa = 0
        D = [A, B, C]
        # MPの計算
        for i in range(3):
            tmpa += abs(sum(cost[i]) - D[i]) + 10*(len(cost[i])-1)
        ans = min(ans, tmpa)

    print(ans)


if __name__ == "__main__":
    main()
