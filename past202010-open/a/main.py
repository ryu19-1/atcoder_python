A, B, C = map(int, input().split())
second = sorted([A, B, C])[1]
print(['A', 'B', 'C'][[A, B, C].index(second)])