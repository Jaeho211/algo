import sys
import math
sys.setrecursionlimit(1000000000)

# https://www.acmicpc.net/problem/4386

# 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
# 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
# 별들이 2차원 평면 위에 놓여 있다.
# 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

# Input Example
# 3
# 1.0 1.0
# 2.0 2.0
# 2.0 4.0


def find(a):
    global parent
    if parent[a] == a:
        return a

    parent[a] = find(parent[a])
    return parent[a]


def merge(a, b):
    global parent
    a = find(a)
    b = find(b)
    if a == b:
        return False

    parent[a] = b
    return True


class Kruskal:
    def __init__(self, prev, next, val):
        self.prev = prev
        self.next = next
        self.val = val


def distance(i, j):
    global stars
    return math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)


n = int(sys.stdin.readline())
stars = []
for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

edge = []

for i in range(n):
    for j in range(n):
        if i != j:
            edge.append(Kruskal(i, j, distance(i, j)))

edge = sorted(edge, key=lambda item: item.val)

cost = 0
parent = [i for i in range(n)]
cnt = 0
for idx in range(len(edge)):
    if merge(edge[idx].next, edge[idx].prev):
        cost += edge[idx].val
        cnt += 1

    if cnt == n - 1:
        break

print(round(cost, 2))
