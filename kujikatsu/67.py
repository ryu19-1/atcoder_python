A, B, C, D, E, F = map(int, input().split())
res = 0
ans = [100*A,0]# sugar+water, sugar

for x in range(F//(100*A)+1):
    for y in range((F-100*A*x)//(100*B)+1):
        if x == y == 0: continue
        sugarMAX = (A*x+B*y)*E
        M = F-100*A*x-100*B*y
        water = 100*A*x+100*B*y
        for z in range(M//C+1):
            for w in range((M-C*z)//D+1):
                sugar = C*z+D*w
                if sugar <= sugarMAX:
                    if ans[1]*(sugar+water) < sugar*ans[0]:
                        ans = [sugar+water, sugar]
                else:
                    break
print(*ans)
