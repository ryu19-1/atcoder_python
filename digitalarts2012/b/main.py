#!/usr/bin/env python3


def main():
    c = input()
    if c == 'z' * 20 or c == 'a':
        print('NO')
    else:
        if len(c) == 1:
            print(chr(ord(c[0])-1)+'a')
        elif sorted(c) != sorted(c, reverse=True):
            if list(c) == sorted(c):
                print(''.join(sorted(c, reverse=True)))
            else:
                print(''.join(sorted(c)))
        else:
            if c[0] == 'z':
                print(c[:-1] + 'ya')
            elif c[0] == 'a':
                print(c[:-2] + 'b')
            else:
                print(c[:-3]+chr(ord(c[0])+1))


if __name__ == "__main__":
    main()
