#!/usr/bin/env python3
from heapq import heappop,heappush

def main():
    N = int(input())
    red = []
    blue = []
    for i in range(N):
        a, b = map(int, input().split())
        red.append([a,b])
    for i in range(N):
        c, d = map(int, input().split())
        blue.append([c,d])
    blue.sort()
    ans = 0

    for i in range(N):
        pairs = []
        for j in range(len(red)):
            x = blue[i][0] - red[j][0]
            y = blue[i][1] - red[j][1]
            if x > 0 and y > 0:
                heappush(pairs, (y,j))

        if len(pairs) > 0:
            ans += 1
            _, index = heappop(pairs)
            del red[index]
    
    print(ans)


    

if __name__ == "__main__":
    main()
