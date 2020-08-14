import sys

sys.setrecursionlimit(1000000000)


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


V, E = map(int, sys.stdin.readline().split())

edge = []
for _ in range(E):
    a, b, weight = map(int, sys.stdin.readline().split())
    edge.append(Kruskal(a, b, weight))

edge = sorted(edge, key=lambda item: item.val)

cost = 0
parent = [i for i in range(V + 1)]
cnt = 0
for idx in range(E):
    if merge(edge[idx].next, edge[idx].prev):
        cost += edge[idx].val
        cnt += 1

    if cnt == V - 1:
        break

print(cost)
