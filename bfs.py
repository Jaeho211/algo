import sys
from collections import deque


# https://www.acmicpc.net/problem/2178

# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# Input Example
# 4 6
# 101111
# 101010
# 101011
# 111011


def move(node, movement):
    global N, M
    new_x = node[0] + movement[0]
    new_y = node[1] + movement[1]
    if 0 <= new_x < M and 0 <= new_y < N:
        return new_x, new_y
    else:
        return node


def bfs(start, end):
    global maze

    visited = [[False] * M for _ in range(N)]

    queue = deque()
    queue.append((start, 1))

    x, y = start
    visited[y][x] = True

    while queue:
        current_node, depth = queue.popleft()

        for movement in movement_array:
            next_node = move(current_node, movement)
            x, y = next_node
            if visited[y][x] == False and maze[y][x] == '1':
                if next_node == end:
                    return depth + 1

                visited[y][x] = True
                queue.append((next_node, depth + 1))

    return -1


N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    row = list(sys.stdin.readline().strip())
    maze.append(row)

movement_array = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]
start = (0, 0)
end = (M - 1, N - 1)
print(bfs(start, end))
