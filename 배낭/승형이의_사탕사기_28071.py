# gold 3

import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph: list, depth):
    visited = set(graph)
    queue = deque(zip(graph, [1] * len(graph)))

    while queue:
        curr_item, curr_depth = queue.popleft()

        if curr_depth >= depth:
            break

        for dx in graph:
            if curr_item + dx not in visited:
                visited.add(curr_item + dx)
                queue.append((curr_item + dx, curr_depth + 1))
    
    return visited

        


N, M, K = map(int, input().split())

candy = list(map(int, input().split()))

ans = 0

for item in sorted(bfs(candy, M), reverse=True):
    if item % K == 0:
        ans = item
        break

print(ans)

