#!/usr/bin/env python3


def main():
    Sd = input()
    N = len(Sd)
    T  = input()
    ans = []
    for i in range(N-len(T)+1):
        flag = True
        tmp = list(Sd)
        for j in range(len(T)):
            if Sd[i+j] == '?':
                tmp[i+j] = T[j]
            elif Sd[i+j] != T[j]:
                flag = False
                break
        if flag:
            ans.append(''.join(tmp).replace('?','a'))
    if ans == []:
        print('UNRESTORABLE')
    else:
        print(sorted(ans)[0])


if __name__ == "__main__":
    main()
