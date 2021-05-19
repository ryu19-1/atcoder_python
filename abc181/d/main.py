#!/usr/bin/env python3


def main():
    S = input()
    N = len(S)
    if N == 1:
        if S == '8':
            print('Yes')
        else:
            print('No')
    elif N == 2:
        a = int(S[0])
        b = int(S[1])
        if (a * 10 + b) % 8 == 0 or (b * 10 + a) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:

        digit = [0] * 10
        for i in range(N):
            digit[int(S[i])] += 1
        # print(digit)
        now = 8
        while now < 1000:
            need = [0] * 10
            k = now
            flag = True
            for i in range(3):
                need[k % 10] += 1
                if k % 10 == 0:
                    flag = False
                k //= 10
            # print(now, need)
            now += 8

            for i in range(1, 10):
                if need[i] > digit[i]:
                    flag = False
                    break
            if flag:
                # print(now, need)
                print('Yes')
                exit()
        print('No')


if __name__ == "__main__":
    main()
