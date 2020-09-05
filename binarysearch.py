import sys

# https://www.acmicpc.net/problem/2512

# 여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.
# 예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자.
# 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다.

# Input Example
# 4
# 120 110 140 150
# 485

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start = 0
end = max(budgets)
while start <= end:
    mid = (start + end) // 2

    total = 0
    for b in budgets:
        total += min(b, mid)

    if total < M:
        start = mid + 1
    elif total > M:
        end = mid - 1
    elif total == M:
        end = mid
        break
print(end)
