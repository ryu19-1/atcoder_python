#!/usr/bin/env python3

def main():
    S = int(input())
    M = 10**9
    if S % M == 0:
        print(0,0,M,0,0,S//M)
    else:
        X = (S+M-1) // M
        a,b,c,d = M,1,M-S%M,X
        print(0,0,a,b,c,d)
        # print(a*d-b*c,S)

if __name__ == "__main__":
    main()
