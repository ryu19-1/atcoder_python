#!/usr/bin/env python3


def main():
    N, S = input().split()
    N = int(N)
    cntA = [0] * N
    cntG = [0] * N
    cntC = [0] * N
    cntT = [0] * N
    for i in range(N):
        if S[i] == 'A':
            cntA[i] += 1
        elif S[i] == 'G':
            cntG[i] += 1
        elif S[i] == 'C':
            cntC[i] += 1
        else:
            cntT[i] += 1
    for i in range(N - 1):
        cntA[i+1] += cntA[i]
        cntG[i+1] += cntG[i]
        cntC[i+1] += cntC[i]
        cntT[i + 1] += cntT[i]
    cntA = [0] + cntA
    cntG = [0] + cntG
    cntC = [0] + cntC
    cntT = [0] + cntT
    ans = 0
    for i in range(N):
        for j in range(i, N):
            if cntA[j + 1] - cntA[i] == cntT[j + 1] - cntT[i] and cntC[j + 1] - cntC[i] == cntG[j + 1] - cntG[i]:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
