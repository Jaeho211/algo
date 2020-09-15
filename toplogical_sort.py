import sys
import heapq

# https://www.acmicpc.net/problem/2251

# N명의 학생들을 키 순서대로 줄을 세우려고 한다.
# 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

# Input Example
# 3 2
# 1 3
# 2 3


N, M = map(int, sys.stdin.readline().split())
adj_list = [[] for i in range(N+1)]
indegree = [0 for i in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    adj_list[A].append(B)
    indegree[B] += 1

queue = []
for idx in range(1, N+1):
    if indegree[idx] == 0:
        heapq.heappush(queue, idx)

result = []
for _ in range(1, N+1):
    idx = heapq.heappop(queue)
    result.append(idx)
    for j in adj_list[idx]:
        indegree[j] -= 1
        if indegree[j] == 0:
            heapq.heappush(queue, j)

print(*result)