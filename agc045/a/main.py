#!/usr/bin/env python3
import math

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        S = input()
        # print(S,A)
        num0 = set()
        num1 = set()
        
        for j in range(N):
            if S[j] == '0':
                num0.add(A[j])
            else:
                num1.add(A[j])
        
        if len(num0) == 0:
            print(1)
        elif len(num1) == 0:
            print(0)
        else:
            digits0 = math.ceil(math.log2(max(num0)+1))
            digits1 = math.ceil(math.log2(max(num1)+1))
            if digits0 < digits1:
                # それぞれのmax(A[i])の対数をとって1の方が大きいと１がかつ
                print(1)
            else:
                if len(num0) < digits0:# 2^digits0の空間を充足できない
                    if num0 == num1:
                        print(0)
                    else:
                        print(1)
                else:# 1,0のベクトルが線型独立か調べる
                    # 各桁のベクトルを保持する
                    vector0 = [[0] * len(num0) for _ in range(digits0)]
                    for i,n in enumerate(num0):
                        for d in range(digits0):
                            vector0[d][i] =  (n >> d) & 1
                    iso_num0 = [0] * digits0
                    for i in range(digits0):
                        iso_num0[i] = sum(vector0[i])

                    vector1 = [[0] * len(num1) for _ in range(digits1)]
                    for i,n in enumerate(num1):
                        for d in range(digits1):
                            vector1[d][i] =  (n >> d) & 1
                    iso_num1 = [0] * digits1
                    for i in range(digits1):
                        iso_num1[i] = sum(vector1[i])
                    
                    print(vector0,vector1)
                    print(iso_num0,digits0)
                    print(iso_num1,digits1)
                    flag = True
                    for i in range(digits1):
                        if iso_num1[i] > 0 and iso_num0[i] == 0:
                            flag = False
                            break
                    if flag:
                        print(0)
                    else:
                        print(1)
        
    

if __name__ == "__main__":
    main()
