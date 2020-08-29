import sys

# https://www.acmicpc.net/problem/12865
#
# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다.
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
# 아직 행군을 해본 적이 없는 준서는 최대 K무게까지의 배낭만 들고 다닐 수 있다.
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

# Input Example
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12


N, LIMIT_WEIGHT = map(int, sys.stdin.readline().split())
dp_dict = {}
for _ in range(N):
    weight, value = map(int, input().split())

    candidate_list = []
    if weight <= LIMIT_WEIGHT:
        candidate_list.append((weight, value))
    else:
        continue

    for accumulated_weight, accumulated_value in dp_dict.items():
        if accumulated_weight + weight <= LIMIT_WEIGHT:
            candidate_list.append((accumulated_weight + weight, accumulated_value + value))

    for accumulated_weight, accumulated_value in candidate_list:
        if dp_dict.get(accumulated_weight, 0) < accumulated_value:
            dp_dict[accumulated_weight] = accumulated_value

if dp_dict:
    print(max(dp_dict.values()))
else:
    print(0)

# N, LIMIT_WEIGHT = map(int, sys.stdin.readline().split())
# things = [(0, 0)]
# for _ in range(N):
#     weight, value = map(int, sys.stdin.readline().split())
#     things.append((weight, value))
#
# dp = [[0] * (LIMIT_WEIGHT + 1) for _ in range(N + 1)]
#
# for n in range(1, N+1):
#     for k in range(1, LIMIT_WEIGHT + 1):
#         if n == 1:
#             if things[1][0] <= LIMIT_WEIGHT and things[1][0] <= k:
#                 dp[1][k] = things[1][1]
#         else:
#             if k-things[n][0] >= 0:
#                 dp[n][k] = max(dp[n-1][k], dp[n-1][k-things[n][0]] + things[n][1])
#             else:
#                 dp[n][k] = dp[n-1][k]
#
# print(dp[n][k])
