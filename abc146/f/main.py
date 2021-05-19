#!/usr/bin/env python3


def main():
    N, M = map(int, input().split())
    S = input()
    if '1' * M in S:
        print(-1)
        exit()

    # 後ろから貪欲にたどる
    ans = []
    now = N
    while now >= 0:
        # print(now, M)
        if now <= M:
            ans.append(now)
            break
        else:
            deme = M
            while deme > 0 and S[now - deme] == '1':
                deme -= 1
            ans.append(deme)
            now -= deme
    print(*ans[::-1])


if __name__ == "__main__":
    main()
