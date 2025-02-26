# gold 5

import sys

input = sys.stdin.readline

H, W = map(int, input().split())

heights = list(map(int, input().split()))

ans = 0

lo, hi = 0, W - 1
left_max, right_max = 0, 0

while lo <= hi:
    # 왼쪽 높이가 오른쪽 높이보다 작을 때
    if heights[lo] < heights[hi]:
        # 왼쪽 최댓값 보다 크면, 그 값으로 갱신
        if heights[lo] >= left_max:
            left_max = heights[lo]
        # 왼쪽 최댓값 보다 작으면 물이 고임
        else:
            ans += left_max - heights[lo]
        lo += 1
    else:
        # 오른쪽 최댓값 보다 크면, 그 값으로 갱신
        if heights[hi] >= right_max:
            right_max = heights[hi]
        # 오른쪽 최댓값 보다 작으면 물이 고임
        else:
            ans += right_max - heights[hi]
        hi -= 1

print(ans)


'''
4 4
3 0 2 0
'''