#!/usr/bin/env python3


def main():
    N = int(input())
    d = len(str(N))
    ansL = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(1,10):
        for j in range(1,10):
            tmp = 0
            # A(1桁)
            if i == j and i <= N:
                tmp += 1
            # AB(2桁)
            if i*10+j <= N:
                tmp += 1
            # A*B(3桁以上d桁未満)
            if d > 2:
                for k in range(3,d):
                    tmp += 10**(k-2)

                # d桁はN以下
                if int(str(N)[0]) > i:
                    tmp += 10**(d-2)
                elif int(str(N)[0]) == i:
                    tmp += int(str(N)[1:-1])
                    if int(str(N)[-1]) >= j:
                        tmp += 1
            ansL[i-1][j-1] = tmp
    
    ans = 0
    for i in range(9):
        for j in range(9):
            ans += ansL[i][j] * ansL[j][i]
    print(ans)
                

if __name__ == "__main__":
    main()
