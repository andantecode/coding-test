# gold 5

# 1번째 사람이 X, 2번째 사람이 O
# 가로, 세로, 대각선 3칸 잇기
# 게임판이 가득 차기

import sys

input = sys.stdin.readline

def solve(status, target="X"):

    # 가로
    for i in range(0, 9, 3):
        if status[i] == target and status[i] == status[i + 1] and status[i] == status[i + 2]:
            return True
    
    # 세로
    for i in range(3):
        if status[i] == target and status[i] == status[i + 3] and status[i] == status[i + 6]:
            return True
        
    # 대각선
    if status[0] == target and status[0] == status[4] and status[0] == status[8]:
        return True
    
    if status[2] == target and status[2] == status[4] and status[2] == status[6]:
        return True
    
    return False

ans = []

while True:
    status = input().strip()

    if status == "end":
        break
    
    number_of_X = status.count("X")
    number_of_O = status.count("O")

    # O가 이긴 경우
    if number_of_X == number_of_O:
        # O가 이기고 X는 져야함
        ans.append(solve(status, "O") and not solve(status, "X"))

    # 가득 찬 경우 또는, X가 이긴 경우
    elif number_of_X == number_of_O + 1:
        # 가득 찬 경우에 O가 이기면 안 됨
        if status.count(".") == 0:
            ans.append(True if not solve(status, "O") else False)
        # X가 이긴 경우 O가 이기면 안 됨
        else:
            ans.append(solve(status, "X") and not solve(status, "O"))
    
    else:
        ans.append(False)


print("\n".join(map(lambda x: "valid" if x else "invalid", ans)))

    
    
