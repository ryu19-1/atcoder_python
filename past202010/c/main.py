#!/usr/bin/env python3


def main():
    N, M = map(int, input().split())
    s = [input() for _ in range(N)]
    ans = [[0]*M for _ in range(N)]
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    for i in range(N):
        for j in range(M):
            res = 0
            if s[i][j] == '#':
                res += 1
            for k in range(8):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < N and 0 <= x < M:
                    if s[y][x] == '#':
                        res += 1
            ans[i][j] = str(res)
    for i in range(N):
        print(''.join(ans[i]))


if __name__ == "__main__":
    main()
