# silver 2

import sys

input = sys.stdin.readline

total_days, number_of_chapters = map(int, input().split())

backpack = []

for _ in range(number_of_chapters):
    backpack.append(list(map(int, input().split())))

dp = [0] * (total_days + 1)

for i in range(number_of_chapters):
    weight, value = backpack[i]
    # 역순으로 탐색
    for days in range(total_days, -1, -1):
        # 만약 현재 챕터를 읽을 수 있다면, 읽는 것과 안 읽는 것을 비교
        if days >= weight:
            dp[days] = max(dp[days], dp[days - weight] + value)
        
            
print(max(dp))
    