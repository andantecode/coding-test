# gold 4

import sys

input = sys.stdin.readline

def get_c(x, y, m):
    h1 = (x**2-m**2)**0.5
    h2 = (y**2-m**2)**0.5

    c = h1*h2 / (h1+h2)

    return c


x, y, c = map(float, input().split())

lo, hi = 0, min(x, y)

while hi - lo > 0.00001:
    
    mid = (lo + hi) / 2

    if get_c(x, y, mid) >= c:
        lo = mid
    else:
        hi = mid

print(lo)