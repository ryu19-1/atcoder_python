#!/usr/bin/env python3


def main():
    N, K = map(int, input().split())
    a = [int(input()) for _ in range(K)]
    a.sort()
    if a[0] == 0:
        i = 1
        seq = []
        while i < K:
            tmp = 1
            while i < K-1 and a[i] + 1 == a[i + 1]:
                tmp += 1
                i += 1
            seq.append((tmp, a[i-tmp+1], a[i]))
            i += 1
        ans = 0
        for j in range(len(seq)-1):
            if seq[j + 1][1] - seq[j][2] > 2:
                continue
            ans = max(ans, seq[j][0] + seq[j + 1][0] + 1)
        print(ans)
    else:
        i = 0
        ans = 0
        while i < K:
            seq = 1
            while i < K-1 and a[i] + 1 == a[i + 1]:
                seq += 1
                i += 1
            ans = max(ans, seq)
            i += 1
        print(ans)


if __name__ == "__main__":
    main()
