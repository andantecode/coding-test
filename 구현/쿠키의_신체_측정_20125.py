# silver 4

import sys

input = sys.stdin.readline

def solve(graph: list, heart: tuple) -> list:
    global size
    ans = [0, 0, 0, 0, 0]

    # 왼쪽 팔
    for i in range(size):
        if graph[heart[0]][i] == "*":
            ans[0] = heart[1] - i
            break
    
    # 오른쪽 팔
    for i in range(size - 1, -1, -1):
        if graph[heart[0]][i] == "*":
            ans[1] = i - heart[1]
            break
    
    leg_y = 0

    # 몸통
    for i in range(heart[0] + 1, size):
        if graph[i][heart[1]] == '_':
            ans[2] = i - heart[0] - 1
            leg_y = i
            break
            
    # 왼쪽 다리
    for i in range(size - 1, leg_y - 1, -1):
        if graph[i][heart[1] - 1] == "*":
            ans[3] = i - leg_y + 1
            break
        

    # 오른쪽 다리
    for i in range(size - 1, leg_y - 1, -1):
        if graph[i][heart[1] + 1] == "*":
            ans[4] = i - leg_y + 1
            break

    return ans

size = int(input())
graph = []
heart = False

for i in range(size):
    temp = input().strip()

    if not heart and "*" in temp:
        heart = (i + 1, temp.index("*"))

    graph.append(temp)

print(" ".join(map(str, map(lambda x: x+1, heart))))
print(" ".join(map(str, solve(graph, heart))))
