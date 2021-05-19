#!/usr/bin/env python3


def main():
    S = input()
    ans = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Si']
    index = [0,2,4,5,7,9,11]
    T = 'WBWBWWBWBWBW'*3
    for i in range(7):
        # print(S[index[i]:index[i]+13])
        if S == T[index[i]:index[i]+20]: 
            print(ans[i])
            exit()


if __name__ == "__main__":
    main()
