#!/usr/bin/env python3

def main():
    H, W = map(int, input().split())
    ans = 0
    now = 0
    
    for i in range(H):
        a, b = map(lambda x: int(x)-1, input().split())
        # print(a,b,now)
        if a <= now <= b:
            ans += b+1-now
            now = b+1
            # print(ans,now)
        if now >= W:
            print(-1)
        else:
            ans += 1
            print(ans)

if __name__ == "__main__":
    main()