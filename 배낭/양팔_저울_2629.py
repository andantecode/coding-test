# gold 3

import sys

input = sys.stdin.readline

num = int(input())

weights = list(map(int, input().split()))
total_weights = sum(weights)

number_of_cases = int(input())

cases = list(map(int, input().split()))

dp = [0] * (total_weights + 1)

dp[weights[0]] = 1

for weight in weights[1:]:
    temp = [0] * (total_weights + 1)
    
    for i in range(total_weights, -1, -1):
        # 원래 가능한 무게에서 현재 추가되는 추를 더해서 만드는 경우 추가
        # i(5)에서 weight(4)를 뺀 무게(1)가 dp 테이블에 존재한다면, dp[i] += 1 (dp[5] += 1)
        if i - weight > 0 and dp[i - weight] > 0:
            temp[i] += 1

        # 원래 가능한 무게에서 현재 추가되는 추를 빼서 만드는 경우 추가
        if i - weight > 0 and dp[i] > 0:
            temp[i - weight] += 1
        
        # 현재 추가되는 추에서 원래 가능한 무게를 빼서 만드는 경우 추가
        # weight(4)에서 i(1)를 뺀 무게(3)을 추가
        if weight - i > 0 and dp[i] > 0:
            temp[weight - i] += 1
        
    # 현재 추의 무게로 만들 수 있는 경우 추가
    temp[weight] += 1

    dp = [previous + now for previous, now in zip(dp, temp)]

    # print(dp)

for case in cases:
    if case > total_weights:
        print("N", end=" ")
        continue
    print("Y" if dp[case] != 0 else "N", end=" ")
print()