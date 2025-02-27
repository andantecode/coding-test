# gold 5

import sys
import heapq
from collections import defaultdict

def dijkstra(graph, points):
    dist = [float("inf")] * (points + 1)
    dist[0], dist[1] = 0, 0

    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        curr_dist, curr_point = heapq.heappop(heap)

        if curr_dist > dist[curr_point]:
            continue

        for point, weight in graph[curr_point]:
            new_dist = curr_dist + weight
            if new_dist < dist[point]:
                heapq.heappush(heap, (new_dist, point))
                dist[point] = new_dist
        
    return dist

input = sys.stdin.readline

points, lines = map(int, input().split())
graph = defaultdict(list)

for _ in range(lines):
    point1, point2, weight = map(int, input().split())

    graph[point1].append((point2, weight))
    graph[point2].append((point1, weight))

print(dijkstra(graph, points)[-1])