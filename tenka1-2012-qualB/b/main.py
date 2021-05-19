#!/usr/bin/env python3


def isword(S):
    if len(S) == 0 or (not S[0].islower()):
        return False

    L = len(S)
    for i in range(1, L):
        if S[i].isupper() or S[i] == '_':
            return False
    else:
        return True


def isCamelCase(S):
    ltrim = 0
    while ltrim < len(S) and S[ltrim] == '_':
        ltrim += 1
    rtrim = 0
    while rtrim < len(S) and S[len(S) - 1 - rtrim] == '_':
        rtrim += 1
    check = S.lstrip('_').rstrip('_')
    arr = []
    N = len(check)
    now = 0
    for i in range(N):
        if check[i].isupper():
            arr.append(check[now:i])
            now = i
    arr.append(check[now:N])
    for i in range(len(arr)):
        if i == 0:
            if not isword(arr[i]):
                return False
        else:
            if arr[i][0].isupper() and '_' not in arr[i]:
                continue
            else:
                return False
    else:
        T = arr[0]
        for i in range(1, len(arr)):
            T += '_' + arr[i][0].lower() + arr[i][1:]
        T = '_'*ltrim + T + '_'*rtrim
        return T


def is_snake_case(S):
    ltrim = 0
    while ltrim < len(S) and S[ltrim] == '_':
        ltrim += 1
    rtrim = 0
    while rtrim < len(S) and S[len(S) - 1 - rtrim] == '_':
        rtrim += 1
    check = S.lstrip('_').rstrip('_')
    arr = check.split('_')
    for i in range(len(arr)):
        if not isword(arr[i]):
            return False
    else:
        T = arr[0]
        for i in range(1, len(arr)):
            T += arr[i][0].upper() + arr[i][1:]
        T = '_'*ltrim + T + '_'*rtrim
        return T


def main():
    S = input()
    if isCamelCase(S) is not False:
        T = isCamelCase(S)
    elif is_snake_case(S) is not False:
        T = is_snake_case(S)
    else:
        T = S
    print(T)


if __name__ == "__main__":
    main()
