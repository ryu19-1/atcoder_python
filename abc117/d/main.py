#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    for d in range(40,-2,-1):# X, Kは高々40bit
        # dはXとKのbitが初めて一致しない桁（全探索している）
        if d != -1 and not (K & (1<<d)):# Kが0の桁はdの候補から外れる
            continue

        tmp = 0
        for e in range(40,-1,-1):# 上の桁から見ていく
            mask = 1<<e# e桁目の数字だけ
            num = 0
            # 配列Aのそれぞれのe桁目のbitの和
            for i in range(N):
                if A[i] & mask:
                    num += 1
            
            if e > d:
                if K & mask:# e桁目が1なので元が0の数だけ立ち上がる
                    tmp += mask*(N-num)
                else:
                    tmp += mask*num
            elif e == d:# K==1よりX==0, よって元が1の数だけ立ち上がる
                tmp += mask*num
            else:# Xが自由に選べるから立ち上がる数が大きくなるようにGreedyに取れる
                tmp += mask*max(num,N-num)
        ans = max(ans,tmp)

    print(ans)

if __name__ == "__main__":
    main()