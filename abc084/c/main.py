#!/usr/bin/env python3


def main():
    N = int(input())
    C = [None] * (N-1)
    S = [None] * (N-1)
    F = [None] * (N-1)
    for i in range(N-1):
        C[i], S[i], F[i] = map(int, input().split())
    
    for i in range(N-1):
        ans = S[i]
        for j in range(i,N-1):
            if j > i:
                if ans <= S[j]:
                    ans = S[j]
                else:
                    if (ans - S[j]) % F[j] > 0:
                        ans += F[j] - (ans - S[j]) % F[j]
            ans += C[j]
        print(ans)
    print(0)


if __name__ == "__main__":
    main()
