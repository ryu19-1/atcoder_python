#!/usr/bin/env python3


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = [['.'] * W for _ in range(H)]
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    checked = [[0]*W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                continue
            flag = True
            for k in range(8):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < H and 0 <= x < W:
                    if S[y][x] == '.':
                        flag = False
                        break
            if flag:
                checked[i][j] = 2
                for k in range(8):
                    y = i + dy[k]
                    x = j + dx[k]
                    if 0 <= y < H and 0 <= x < W:
                        if S[y][x] == '#' and checked[y][x] == 0:
                            checked[y][x] = 1
    # print(checked)
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                if checked[i][j] == 1:
                    print('impossible')
                    exit()
                else:
                    continue
            if checked[i][j] == 2:
                # print(i, j)
                ans[i][j] = '#'
            elif checked[i][j] == 0:
                print('impossible')
                exit()
    print('possible')
    [print(''.join(a)) for a in ans]


if __name__ == "__main__":
    main()
