# silver 3

import sys

input = sys.stdin.readline

total, now = map(int, input().split())

win_rate = (now * 100) // total

if win_rate >= 99:
    print(-1)

else:
    start, end = 0, total

    while start < end:
        mid = (start + end) // 2
        new_win_rate = ((now + mid) * 100) // (total + mid)

        if new_win_rate > win_rate:
            # 현재의 mid 값이 ans가 될 수 있기 때문에 end = mid로 갱신
            end = mid
        else:
            start = mid + 1
        
    print(start)