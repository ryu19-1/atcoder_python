#!/usr/bin/env python3


def main():
    S = input()
    S = S[1:-1]
    N = len(S)
    # print(S)
    check = [0] * (N+1)
    for i in range(N):
        check[i+1] = check[i]
        if S[i] == '{':
            check[i+1] += 1
        elif S[i] == '}':
            check[i + 1] -= 1
    T = ''
    for i in range(N):
        if check[i + 1] == 0 and check[i] == 0:
            T += S[i]
    # print(T)
    if ':' in T or T == '':
        print('dict')
    else:
        print('set')


if __name__ == "__main__":
    main()
