# silver 3

import sys

input = sys.stdin.readline

N, L, W, H = map(int, input().split())

lo, hi = 0, max(L, W, H)

for _ in range(10000):
    mid = (lo + hi) / 2

    if (W // mid) * (H // mid) * (L // mid) < N:
        hi = mid
    else:
        lo = mid
    
print(lo)
