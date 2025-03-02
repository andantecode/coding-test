# silver 2

import sys

input = sys.stdin.readline

N = int(input())

deposit = list(map(int, input().split()))

total = int(input())

ans = 0
lo, hi = 1, max(deposit)

while lo <= hi:
    mid = (lo + hi) // 2

    temp_total = 0

    for item in deposit:
        if item >= mid:
            temp_total += mid
        else:
            temp_total += item

    if temp_total > total:
        hi = mid - 1
    else:
        ans = mid
        lo = mid + 1

print(ans)