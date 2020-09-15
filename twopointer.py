import sys

# https://www.acmicpc.net/problem/1806

# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
# 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

# Input Example
# 10 15
# 5 1 3 5 10 7 4 9 2 8


N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

low = -1
high = 0
length = float('inf')
partial_sum = numbers[0]
while low <= high < N:
    if partial_sum < S:
        high += 1
        if high == N:
            break
        partial_sum += numbers[high]
    elif partial_sum == S:
        length = min(length, high-low)
        high += 1
        if high == N:
            break
        partial_sum += numbers[high]
    else:
        length = min(length, high-low)
        low += 1
        partial_sum -= numbers[low]

    # print(low, high, partial_sum)

if length == float('inf'):
    print(0)
else:
    print(length)