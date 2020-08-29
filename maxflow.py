import sys
from collections import deque


# https://www.acmicpc.net/problem/17412

# N개의 도시가 P개의 단방향 길로 연결되어 있다. 이석원은 1번 도시와 2번 도시 사이를 가며 워해머를 한다.
# 성실한 이석원은 1번에서 2번으로 가는 서로 다른 경로를 최대한 많이 찾으려고 하는데, 이때 한 경로에 포함된 길이 다른 경로에 포함되면 안된다.
# 입력에는 1번 도시와 2번 도시를 연결하는 길은 없다. 도시의 번호는 1번부터 N번 까지이다.

# Input Example
# 5 5
# 1 3
# 3 2
# 1 5
# 5 4
# 4 2


class NetworkFlow:
    def __init__(self, N, capacity, adj):
        self.N = N
        self.capacity = capacity
        self.adj = adj

    def bfs(self, flow, source, sink):
        parent = [-1]*self.N
        q = deque()
        q.append(source)
        parent[source] = source
        while q:
            u = q.popleft()
            for v in self.adj[u]:
                if parent[v] != -1:
                    continue

                if self.capacity[u][v] - flow[u][v] > 0:
                    q.append(v)
                    parent[v] = u

                    if v == sink:
                        break
        return parent

    def max_flow(self, source, sink):
        flow = [[0]*self.N for _ in range(self.N)]
        total_flow = 0
        while True:
            parent = self.bfs(flow, source, sink)
            if parent[sink] == -1:
                break

            amount = float('inf')
            p = sink
            while p != source:
                amount = min(amount, self.capacity[parent[p]][p] - flow[parent[p]][p])
                p = parent[p]

            p = sink
            while p != source:
                flow[parent[p]][p] += amount
                flow[p][parent[p]] -= amount
                p = parent[p]
            total_flow += amount
        return total_flow


N, P = map(int, sys.stdin.readline().split())
SOURCE = 1
SINK = 2
capacity = [[0]*(N+1) for _ in range(N+1)]
adj = [[] for _ in range(N+1)]
for _ in range(P):
    city1, city2 = map(int, sys.stdin.readline().split())
    capacity[city1][city2] = 1
    adj[city1].append(city2)
    adj[city2].append(city1)

network_flow = NetworkFlow(N+1, capacity, adj)
res = network_flow.max_flow(SOURCE, SINK)
print(res)
