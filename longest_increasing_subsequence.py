import sys
import bisect

# bisect module을 사용하든 직접 구현하든 시간은 거의 차이 없음.
# https://www.acmicpc.net/problem/11053

# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# Input Example
# 6
# 10 20 10 30 20 50

# def bisect_left(x):
#     lo = 0
#     hi = len(li_sequence)
#     while lo < hi:
#         mid = (lo+hi)//2
#         if li_sequence[mid] < x:
#             lo = mid+1
#         else:
#             hi = mid
#     return lo


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

li_sequence = [numbers[0]]
for idx in range(1, N):
    if li_sequence[-1] < numbers[idx]:
        li_sequence.append(numbers[idx])
    else:
        idx_li_sequence = bisect.bisect_left(li_sequence, numbers[idx])
        # idx_li_sequence = bisect_left(numbers[idx])
        li_sequence[idx_li_sequence] = numbers[idx]

print(len(li_sequence))