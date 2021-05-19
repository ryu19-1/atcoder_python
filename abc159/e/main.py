#!/usr/bin/env python3


def main():
    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]
    cnt = [[0] * (H) for _ in range(W+1)]
    INF = 10**12
    for i in range(H):
        for j in range(W):
            if S[i][j] == '1':
                cnt[j+1][i] = 1
            if j > 0:
                cnt[j+1][i] += cnt[j][i]
    ans = INF
    for i in range(1 << (H - 1)):
        divide = [0]
        for j in range(H-1):
            if (i >> j) & 1:
                divide.append(j + 1)
        divide.append(H)
        res = len(divide)-2
        l = 0
        r = 1
        check = cnt[r][:]
        flag = True
        while r <= W:
            for h in range(len(divide) - 1):
                if sum(check[divide[h]:divide[h + 1]]) > K:
                    if l == r - 1:
                        flag = False
                    else:
                        res += 1
                        l = r - 1
                    break
            else:
                r += 1
            if r == W+1:
                break
            if flag == False:
                break
            for k in range(H):
                check[k] = cnt[r][k]-cnt[l][k]
        if flag:
            ans = min(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
