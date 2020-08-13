import sys

# https://www.acmicpc.net/problem/1725

# 주어진 히스토그램에 대해, 가장 큰 직사각형의 넓이를 구하는 프로그램을 작성하시오.

# Input Example
# 7
# 2
# 1
# 4
# 5
# 1
# 3
# 3


def divideandconquer(start, end):
    global histogram
    if start == end:
        return histogram[start]

    mid = (start + end) // 2
    area1 = divideandconquer(start, mid)
    area2 = divideandconquer(mid + 1, end)

    max_area = max(area1, area2)
    u = mid
    v = mid + 1
    min_height = min(histogram[u], histogram[v])
    max_area = max(max_area, min_height * 2)
    while u > start and v < end:
        if histogram[u - 1] > histogram[v + 1]:
            u -= 1
            min_height = min(min_height, histogram[u])
            max_area = max(max_area, min_height * (v - u + 1))
        else:
            v += 1
            min_height = min(min_height, histogram[v])
            max_area = max(max_area, min_height * (v - u + 1))

    if u == start:
        while v < end:
            v += 1
            min_height = min(min_height, histogram[v])
            max_area = max(max_area, min_height * (v - u + 1))
    else:
        while u > start:
            u -= 1
            min_height = min(min_height, histogram[u])
            max_area = max(max_area, min_height * (v - u + 1))

    return max_area


N = int(sys.stdin.readline())
histogram = []
for _ in range(N):
    histogram.append(int(sys.stdin.readline()))

res = divideandconquer(0, N - 1)
print(res)
