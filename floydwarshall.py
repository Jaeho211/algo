import sys
from collections import deque
import heapq


# https://www.acmicpc.net/problem/11404

# n(1 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다.
# 각 버스는 한 번 사용할 때 필요한 비용이 있다.
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

# Input Example
# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4


def floyd_warshall():
    for k in range(1, N + 1):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:  # 자기 자신으로 오는 경우는 없다고 했으므로
                    visited[i][j] = 0
                else:  # 경로 거치는 것 or 직접 가는 것 or 이전 경로들
                    visited[i][j] = min(visited[i][j],
                                        visited[i][k] + visited[k][j])


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
visited = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    city1, city2, cost = map(int, sys.stdin.readline().split())
    visited[city1][city2] = min(cost, visited[city1][city2])

floyd_warshall()
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if visited[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
