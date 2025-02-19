# gold 4

import sys
import heapq

input = sys.stdin.readline

def dijkstra(graph, start_point):
    # 초기화 (시작점은 0, 나머지는 inf)
    dist = [float("inf")] * (len(graph) + 1)
    dist[start_point] = 0

    # 우선순위 큐 (가장 거리가 짧은 것을 기준으로 탐색해야 함)
    heap = []
    heapq.heappush(heap, (0, start_point))

    while heap:
        curr_dist, curr_point = heapq.heappop(heap)

        # 만약 힙에서 꺼낸 값이 이미 들어간 값보다 크다면 갱신할 필요가 없음
        if dist[curr_point] < curr_dist:
            continue

        # 힙에서 꺼낸 노드와 연결된 노드들 갱신
        for (point, weight) in graph[curr_point]:
            new_dist = curr_dist + weight
            if new_dist < dist[point]:
                dist[point] = new_dist
                heapq.heappush(heap, (new_dist, point))

    return dist


vertices, edges = map(int, input().split())

graph = {i + 1: [] for i in range(vertices)}

start_point = int(input())

for i in range(edges):
    point1, point2, weight = map(int, input().split())

    graph[point1].append((point2, weight))



dist = dijkstra(graph, start_point)

for i in range(1, vertices + 1):
    print(dist[i] if dist[i] != float('inf') else "INF")


