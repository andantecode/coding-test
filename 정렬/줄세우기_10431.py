# silver 5

import sys

input = sys.stdin.readline

# 자기 앞에 자기보다 큰 학생이 없다면 그냥 그 자리에 선다.
# 자기 앞에 자기보다 큰 학생이 있다면, 그 중 가장 앞에 있는 학생의 바로 앞에 서고, 뒤의 학생은 1칸씩 물러난다.
def solve(heights: list) -> int:
    length = len(heights)
    count = 0

    for i in range(length):
        for j in range(i):
            if heights[j] > heights[i]:
                temp = heights.pop(i)
                heights.insert(j, temp)
                count += (i - j)
                break

    return count


number_of_cases = int(input())

for i in range(number_of_cases):
    _, heights = input().strip().split(maxsplit=1)
    heights = list(map(int, heights.split()))
    print(i + 1, solve(heights))

    