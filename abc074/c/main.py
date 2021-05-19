#!/usr/bin/env python3


def main():
    A, B, C, D, E, F = map(int, input().split())
    ans = [100*A,0]
    # 水の量で全探索する
    N = F // (100*A)
    M = F // (100*B)
    for i in range(N+1):
        for j in range(M+1):
            if i == j == 0:# 水なしはだめ
                continue
            water = 100*A*i + 100*B*j
            if water > F:
                continue
            K = (F - water) // C
            L = (F - water) // D
            for k in range(K+1):
                for l in range(L+1):
                    sugar = C*k + D*l
                    if sugar > (A*i + B*j) * E:# 溶け残りはだめ
                        continue
                    if water + sugar > F:# 溢れたらだめ
                        continue
                    if ans[1] / ans[0] < sugar / (sugar+water):
                        ans = [water+sugar, sugar]
            
    print(*ans)
                    

if __name__ == "__main__":
    main()
