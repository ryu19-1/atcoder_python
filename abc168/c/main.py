#!/usr/bin/env python3
import math

def main():
    A, B, H, M = map(int, input().split())
    s = 30*H+0.5*M
    l = 6 * M
    C = A**2 + B**2 - 2*A*B*math.cos(math.radians(abs(l-s)))
    print(C**0.5)

if __name__ == "__main__":
    main()
