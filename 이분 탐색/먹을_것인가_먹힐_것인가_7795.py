# silver 3

import sys

input = sys.stdin.readline

number_of_case = int(input())

for _ in range(number_of_case):
    number_of_A, number_of_B = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    B = sorted(B)

    for item in A:
        lo, hi = 0, len(B) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if B[mid] >= item:
                hi = mid - 1
            else:
                lo = mid + 1

        ans += lo
    
    print(ans)