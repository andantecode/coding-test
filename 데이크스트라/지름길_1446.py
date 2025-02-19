# silver 1

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def dijkstra(graph, target_length):
    dist = [float("inf")] * (target_length + 1)
    dist[0] = 0

    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        curr_dist, curr_point = heapq.heappop(heap)

        if dist[curr_point] < curr_dist:
            continue

        for item, weight in graph[curr_point]:
            if item <= target_length and curr_dist + weight < dist[item]:
                dist[item] = curr_dist + weight
                heapq.heappush(heap, (curr_dist + weight, item))

    return dist

path, target_length = map(int, input().split())
graph = defaultdict(list)
for i in range(target_length):
    graph[i].append((i + 1, 1))

for i in range(path):
    start, end, length = map(int, input().split())

    graph[start].append((end, length))

dist = dijkstra(graph, target_length)

print(dist[-1])