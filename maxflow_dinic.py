import sys
from collections import deque, defaultdict
sys.setrecursionlimit(1000000000)

# https://www.acmicpc.net/problem/2316

# N개의 도시가 P개의 양방향 길로 연결되어 있다.
# 성실한 이석원은 두 도시 사이를 최대한 많이 왔다 갔다 하려 하는데, 이때 한 번 방문했던 도시(1, 2번 도시 제외)를 두 번 이상 방문하지 않으려 한다.
# 한 번 1번 도시와 2번 도시 사이를 오갈 때, 반드시 한 개 이상의 도시를 중간에 거쳐야 한다. 입력에는 1번 도시와 2번 도시를 연결하는 길은 없다.
# 도시의 번호는 1번부터 N번까지이다.

# Input Example
# 7 8
# 1 3
# 1 4
# 3 5
# 4 5
# 5 6
# 5 7
# 6 2
# 7 2


class Dinic:
    def __init__(self, N, source: int, sink: int):
        self.N = N
        self.g = defaultdict(lambda: defaultdict(lambda: 0))
        self.source = source
        self.sink = sink
        self.total_flow = 0
        self.cut = defaultdict(lambda: False)

    def set_source(self, s):
        self.source = s

    def set_sink(self, s):
        self.sink = s

    def bfs(self, level_of: list):
        queue = deque()
        queue.append(self.source)

        while queue:
            node = queue.popleft()
            level = level_of[node]

            for child in self.g[node].keys():
                if level_of[child] == -1 and self.g[node][child] > 0:
                    level_of[child] = level + 1
                    queue.append(child)

    def dfs(self, level_of: list, node: int, visited: defaultdict, paths: list):
        if visited[node]:
            return
        visited[node] = True
        paths.append(node)

        for child in self.g[node].keys():
            if level_of[child] - level_of[node] == 1 and self.g[node][child] > 0:
                self.dfs(level_of, child, visited, paths)

        min_capacity = float('inf')
        if node == self.sink:
            visited[node] = False

            s = self.source
            for node_t in paths[1:]:
                if self.g[s][node_t] < min_capacity:
                    min_capacity = self.g[s][node_t]
                s = node_t

            self.total_flow += min_capacity
            s = self.source
            for node_t in paths[1:]:
                self.g[s][node_t] -= min_capacity
                self.g[node_t][s] += min_capacity
                s = node_t

        paths.pop()

    def get_graph(self):
        return self.g

    def get_maximum_flow(self):
        while True:
            level_of = [-1] * self.N
            level_of[self.source] = 0
            self.bfs(level_of)
            if level_of[self.sink] == -1:
                break
            visited = defaultdict(lambda: False)
            paths = []
            self.dfs(level_of, self.source, visited, paths)
        return self.total_flow

    def get_cut(self, node: int):
        if self.cut[node]:
            return
        self.cut[node] = True

        for child in self.g[node].keys():
            if self.g[node][child] > 0:
                self.get_cut(child)


N, P = map(int, sys.stdin.readline().split())
SOURCE = 1 * 2 + 1
SINK = 2 * 2
dinic = Dinic((N+1)*2, SOURCE, SINK)
graph = dinic.get_graph()
for city in range(1, N+1):
    city_in = 2 * city
    city_out = 2 * city + 1
    graph[city_in][city_out] = 1
    graph[city_out][city_in] = 0

for _ in range(P):
    city1, city2 = map(int, sys.stdin.readline().split())
    city1_in = 2 * city1
    city1_out = 2 * city1 + 1
    city2_in = 2 * city2
    city2_out = 2 * city2 + 1
    graph[city1_out][city2_in] = 1
    graph[city2_in][city1_out] = 0
    graph[city2_out][city1_in] = 1
    graph[city1_in][city2_out] = 0

total_flow = dinic.get_maximum_flow()
print(total_flow)
