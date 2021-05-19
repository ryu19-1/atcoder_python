#!/usr/bin/env python3

def main():
    R, C, K = map(int, input().split())
    s = [input() for _ in range(R)]

    # 方針: TLEするので再利用が必要。菱形の中心になるには、左右方向にK-1個のシロマスが連続している必要がある
    sleft = []# 左方向の連続数
    sright  = []# 右方向の連続数
    for i in range(R):
        tmp = [None] * C
        if s[i][0] == 'o':
            tmp[0] = 1
        else:
            tmp[0] = 0
        for j in range(1,C):
            if s[i][j] == 'o':
                tmp[j] = tmp[j-1]+1
            else:
                tmp[j] = 0
        sleft.append(tmp)

    for i in range(R):
        tmp = [None] * C
        if s[i][-1] == 'o':
            tmp[-1] = 1
        else:
            tmp[-1] = 0
        for j in range(C-2,-1,-1):
            if s[i][j] == 'o':
                tmp[j] = tmp[j+1]+1
            else:
                tmp[j] = 0
        sright.append(tmp)
    # print(sright)
    # print(sleft)
    # print(s)
    
    ans = 0
    for i in range(K-1,R-K+1):
        for j in range(K-1,C-K+1):
            if sright[i][j] < K or sleft[i][j] < K: continue
            for k in range(K-1,0,-1):# 上下方向に移動
                # print(i,j,k)
                if sright[i+(K-k)][j] < k or sleft[i+(K-k)][j] < k:
                    break
                elif sright[i-(K-k)][j] < k or sleft[i-(K-k)][j] < k:
                    break
            else:
                ans += 1
                # print(i,j,ans)
    print(ans)

if __name__ == "__main__":
    main()