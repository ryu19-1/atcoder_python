#!/usr/bin/env python3


def main():
    T = list(input())
    N = len(T)
    i = 0
    while i < N:
        if T[i] == '?':
            if i == 0 or i == N-1:
                T[i] = 'D'
            elif T[i-1] == 'D':
                if T[i+1] == '?':
                    T[i] = 'P'
                    T[i+1] = 'D'
                    i += 1
                elif T[i+1] == 'D':
                    T[i] = 'P'
                else:
                    T[i] = 'D'
            else:
                T[i] = 'D'
        i += 1
    print(''.join(T))

if __name__ == "__main__":
    main()
