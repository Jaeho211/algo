import sys
from collections import deque
import heapq

# https://www.acmicpc.net/problem/1916

# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

# Input Example
# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5

# def bfs(start, end):
#     visited = [float('inf')]*(N+1)
#
#     queue = deque()
#     queue.append((start, 0))
#
#     while queue:
#         current_node, current_cost = queue.popleft()
#         if visited[current_node] < current_cost:
#             continue
#
#         for next_node, next_cost in graph[current_node]:
#             next_cost_sum = current_cost + next_cost
#             if next_node == end:
#                 visited[next_node] = min(visited[next_node], next_cost_sum)
#                 continue
#
#             if next_cost_sum < visited[next_node] and next_cost_sum < visited[next_node]:
#                 queue.append((next_node, next_cost_sum))
#                 visited[next_node] = next_cost_sum
#
#     return visited[end]


def dijkstra(start, end):
    visited = [float('inf')] * (N + 1)

    visited[start] = 0
    heap = []
    heapq.heappush(heap, (start, 0))

    while heap:
        current_node, current_cost = heapq.heappop(heap)
        if visited[current_node] < current_cost:
            continue

        for next_node, next_cost in graph[current_node]:
            next_cost_sum = current_cost + next_cost
            if next_node == end:
                visited[next_node] = min(visited[next_node], next_cost_sum)
                continue

            if next_cost_sum < visited[next_node]:
                heapq.heappush(heap, (next_node, next_cost_sum))
                visited[next_node] = next_cost_sum

    return visited[end]


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    city1, city2, cost = map(int, sys.stdin.readline().split())
    graph[city1].append((city2, cost))

start, end = map(int, sys.stdin.readline().split())
print(dijkstra(start, end))
# print(bfs(start, end))

