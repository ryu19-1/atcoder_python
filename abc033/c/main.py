#!/usr/bin/env python3


def main():
    S = input()
    ans = 0
    for l in S.split('+'):
        if len(l) == 1 and l != '0':
            ans += 1
        elif '0' not in l:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
