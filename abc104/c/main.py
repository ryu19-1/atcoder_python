#!/usr/bin/env python3

def main():
    D, G = map(int, input().split())
    p = [None] * D
    c = [None] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    
    ans = 10**18
    for i in range(2**D):
        tmp = 0
        score = 0
        k = 0
        for j in range(D):
            if (i >> j) & 1:
                score += p[j]*100*(j+1) + c[j]
                tmp += p[j]
            else:
                k = j
        tmp2 = 0
        while score < G and tmp2 < p[k]:
            score += 100 * (k+1)
            tmp2 += 1
        if score >= G:
            ans = min(ans,tmp+tmp2)
            # print(i,tmp,score)
    print(ans)



if __name__ == "__main__":
    main()
