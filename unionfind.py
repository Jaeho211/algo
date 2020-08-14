import sys
sys.setrecursionlimit(1000000000)

# https://www.acmicpc.net/problem/10775

# 공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.
# 공항에는 P개의 비행기가 순서대로 도착할 예정이며, 당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다.
# 비행기가 도킹된 게이트에는 다른 비행기가 도착할 수 없다.
# 이러한 사고가 일어나면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.
# 승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?

# Input Example
# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4


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
        return

    parent[a] = b
    return


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
gates = [False]*(G+1)
parent = [i for i in range(G+1)]
finished = False
for _ in range(P):
    gate = int(sys.stdin.readline())
    if gates[gate] is False:
        gates[gate] = True
        if gate > 1:
            merge(gate, gate-1)
    elif gates[find(gate)] is False:
        gates[find(gate)] = True
        if find(gate) > 1:
            merge(find(gate), find(gate)-1)
    else:
        break

print(sum(gates))


# G = int(sys.stdin.readline())
# P = int(sys.stdin.readline())
# gates = [False]*(G+1)
# finished = False
# for _ in range(P):
#     gate = int(sys.stdin.readline())
#     if finished:
#         continue
#
#     check_finished = False
#     for candidate in range(gate, 0, -1):
#         if gates[candidate] is False:
#             gates[candidate] = True
#             check_finished = True
#             break
#
#     if check_finished is False:
#         print(sum(gates))
#         finished = True