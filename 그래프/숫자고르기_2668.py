# gold 5

# 첫째 줄에서 선택을 하면, 둘째 줄의 값이 첫째 줄에 다시 선택된다.
# 사이클을 찾는 문제인 것 같음

import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph: list, start_point: int):
    visited = set([])
    queue = deque([start_point])

    while queue:
        point = queue.popleft()

        if graph[point] not in visited:
            visited.add(graph[point])
            queue.append(graph[point])
    
    return visited


size = int(input())
graph = [0]

for i in range(size):
    graph.append(int(input()))

ans = set()

for i in range(size):
    temp_visited = bfs(graph, i + 1)

    if i + 1 in temp_visited:
        ans = ans.union(temp_visited)

ans = sorted(ans)
print(len(ans))
print("\n".join(map(str, ans)))
