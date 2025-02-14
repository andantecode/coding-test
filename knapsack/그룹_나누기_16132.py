# gold 4

import sys

input = sys.stdin.readline

n = int(input())

factory = list(range(1, n + 1))
total = sum(factory)

# 합이 홀수라면 불가능
if total % 2 != 0:
    print(0)

# 짝수라면 나누기 2를 한 것을 만드는 경우의 수 구하기
else:
    length = total // 2 + 1
    # DP 테이블 각각의 위치에 그 수를 만들 수 있는 경우의 수를 저장
    dp = [0] * length

    # i번째 item까지 고려하면서 DP 테이블 갱신
    for item in factory:
        # 먼저, 해당 item을 단일로 넣는 경우의 수를 더해줌
        dp[item] = dp[item] + 1

        # 역순으로 갱신 (최대 합부터 item까지 검사)
        for i in range(length - 1, item, -1):

            # 만약, i - item을 만들 수 있는 경우의 수가 존재한다면
            # 그 경우의 수에 + item을 하면 i를 만들 수 있음
            if dp[i - item] != 0:
                if i - item != item:
                    dp[i] += dp[i - item]
                # 다만, item을 단일로 넣은 경우는 빼줘야 함 (2를 넣고, 4를 검사할 때 2+2가 포함되는 것을 방지)
                # 즉, 4 - 2가 2와 같은 경우에는 2를 만드는 경우의 수에서 1을 빼서 더해줌 (dp[item] = dp[item] + 1로 더해진 상황은 빼기)
                else:
                    dp[i] += (dp[i - item] - 1)
                
    print(dp[-1] // 2)
        




