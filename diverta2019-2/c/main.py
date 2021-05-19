#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    pos = []
    neg = []
    for i in range(N):
        if A[i] >= 0:
            pos.append(A[i])
        else:
            neg.append(A[i])
    pos.sort()
    neg.sort(reverse=True)
    
    # N個のうち、最低1つは符号を変える＆最低１つは符号をかえない
    ans = []
    if len(pos) == 0:# 負だけ
        print(-sum(neg)+2*neg[N-1])
        now = neg[0]
        for i in range(1,N):
            print(now,neg[i])
            now -= neg[i]
    elif len(neg) == 0:# 正だけ
        print(sum(pos)-2*pos[0])
        now = pos[0]
        for i in range(1,N-1):
            print(now,pos[i])
            now -= pos[i]
        print(pos[N-1],now)
    else:
        p = 0
        n = 1
        ans = []
        now = pos[p]
        while n < len(neg):
            ans.append((now,neg[n]))
            now -= neg[n]
            n += 1
        
        p += 1
        now2 = neg[0]
        while p < len(pos):
            ans.append((now2,pos[p]))
            now2 -= pos[p]
            p += 1
        
        ans.append((now,now2))
        print(now-now2)
        for a in ans:
            print(a[0],a[1])

if __name__ == "__main__":
    main()
