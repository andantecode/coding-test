# silver 4

import sys

input = sys.stdin.readline

number_of_buses, time = map(int, input().split())

ans = []

for _ in range(number_of_buses):
    start_time, gap, count = map(int, input().split())

    times = list(range(start_time, start_time + gap * count, gap))

    if time <= times[-1]:
        start, end = 0, count - 1

        while start <= end:
            mid = (start + end) // 2

            if times[mid] > time:
                end = mid - 1
            elif times[mid] < time:
                start = mid + 1
            else:
                start = mid
                break

        ans.append(times[start] - time)
    
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
    
        
    