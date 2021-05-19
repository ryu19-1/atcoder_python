class ModInt:
    def __init__(self, x, MOD):
        self.x = x % MOD
        self.m = MOD

    def __add__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.x + other.x, self.m)
        else:
            return ModInt(self.x + other, self.m)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.x - other.x, self.m)
        else:
            return ModInt(self.x - other, self.m)

    def __rsub__(self, other):
        if isinstance(other, ModInt):
            return ModInt(other.x - self.x, self.m)
        else:
            return ModInt(other - self.x, self.m)

    def __pow__(self, other):
        if isinstance(other, ModInt):
            return ModInt(pow(self.x, other.x, self.m), self.m)
        else:
            ModInt(pow(self.x, other, self.m), self.m)

    def __rpow__(self, other):
        if isinstance(other, ModInt):
            return ModInt(pow(other.x, self.x, self.m), self.m)
        else:
            ModInt(pow(other, self.x, self.m), self.m)

N = int(input())
X = list(map(int, input()))
Xc = sum(X)

if Xc == 0:
    [print(1) for i in range(N)]
elif Xc == 1:
    ans1 = ModInt(0, Xc+1)
    for j in range(N):
        if X[j]:
            ans1 += pow(2,N-1-j,Xc+1)

    for j in range(N):
        if X[j]:
            print(0)
        else:
            print(2) if X[N-1] or j == N-1 else print(1)
else:
    ans1 = ModInt(0, Xc+1)
    ans2 = ModInt(0, Xc-1)
    for j in range(N):
        if X[j]:
            ans1 += pow(2,N-1-j,Xc+1)
            ans2 += pow(2,N-1-j,Xc-1)

    for i in range(N):
        if X[i]:# 1->0
            ans = ans2 - pow(2,N-1-i,Xc-1)
        else:# 0->1
            ans = ans1 + pow(2,N-1-i,Xc+1)
        count = 1
        while ans.x > 0:
            tmp = str(bin(ans.x)).count('1')
            ans.x %= tmp
            count += 1
        print(count)