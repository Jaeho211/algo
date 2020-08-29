import sys

sys.setrecursionlimit(1000000000)


# https://www.acmicpc.net/problem/1520

# 여행을 떠난 세준이는 지도를 하나 구하였다. 이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다.
# 한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.
# 지도가 주어질 때 이와 같이 제일 왼쪽 위 지점에서 출발하여
# 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

# Input Example
# 4 5
# 50 45 37 32 30
# 35 50 40 20 25
# 30 30 25 17 28
# 27 24 22 15 10


def dfs(x, y):
    global matrix, dp
    if dp[y][x] != -1:
        return dp[y][x]

    if x == N - 1 and y == M - 1:
        return 1

    dp[y][x] = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_x = x + dx
        next_y = y + dy

        if 0 <= next_x < N and 0 <= next_y < M and \
                matrix[y][x] > matrix[next_y][next_x]:
            dp[y][x] += dfs(next_x, next_y)

    return dp[y][x]


M, N = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(M):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1] * N for _ in range(M)]
count = dfs(0, 0)
print(count)
