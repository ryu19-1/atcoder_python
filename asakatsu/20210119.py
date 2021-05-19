T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

C1 = A1 - B1
C2 = A2 - B2
if C1 < 0:
    C1 = -C1
    C2 = -C2
if T1 * C1 + T2 * C2 == 0:
    print('infinity')
elif T1 * C1 + T2 * C2 > 0:
    print(0)
else:
    diff = abs(T2 * C2 + T1 * C1)
    res = abs(T1 * C1) // diff
    if abs(T1 * C1) % diff == 0:
        print(1 + res*2)
    else:
        print(2 + res*2)
