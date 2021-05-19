#!/usr/bin/env python3
def main():
    N = int(input())
    if N == 1:print(1);exit();
    x = [None] * N
    y = [None] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    
    diff = []
    nums = []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if (x[j]-x[i],y[j]-y[i]) in diff:
                nums[diff.index((x[j]-x[i],y[j]-y[i]))] += 1
            else:
                diff.append((x[j]-x[i],y[j]-y[i]))
                nums.append(1)
    # print(diff)
    # print(nums)
    print(N-max(nums))

if __name__ == "__main__":
    main()
