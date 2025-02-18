# silver 4

import sys

# 남학생: 받은 수의 배수 스위치 변경
# 여학생: 받은 수 기준으로 거리가 같은 index에 대해 같은 상태라면 가장 넓은 범위에 거쳐 모두 변경

def update_switches(switches, gender, idx):
    # 남자
    if gender == 1:
        # idx 기준으로, idx, idx + number, idx + 2*number,...  (0-based)
        # 즉, step = (idx+1) 이고 start = idx
        step = idx + 1
        for i in range(idx, len(switches), step):
            switches[i] ^= 1
    # 여자
    else:
        # 중심이 idx인 상태에서 양옆으로 확장
        left = idx
        right = idx
        # 먼저 자기 자신 토글
        switches[idx] ^= 1

        # 그 다음 양옆 비교
        while left > 0 and right < len(switches) - 1:
            if switches[left - 1] == switches[right + 1]:
                left -= 1
                right += 1
                switches[left] ^= 1
                switches[right] ^= 1
            else:
                break

    return switches


input = sys.stdin.readline

number_of_switches = int(input())
switches = list(map(int, input().split()))

number_of_cases = int(input())
for _ in range(number_of_cases):
    gender, number = map(int, input().split())

    switches = update_switches(switches, gender, number - 1)

for i in range(len(switches)):
    # 스위치 상태 출력 (띄어쓰기)
    print(switches[i], end=' ')
    
    # 20개 출력할 때마다 줄바꿈
    if (i + 1) % 20 == 0:
        print()

# 만약 마지막 줄이 20개 미만으로 끝났다면, 
# 위 if문에서 줄바꿈이 일어나지 않으므로 한 줄 비워주기
if len(switches) % 20 != 0:
    print()
