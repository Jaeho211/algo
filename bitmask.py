import sys

# https://www.acmicpc.net/problem/11723

# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

N = int(sys.stdin.readline())
global_set = 0
for _ in range(N):
    calculation = list(sys.stdin.readline().split())

    if len(calculation) == 1:
        if calculation[0][0] == 'a':
            global_set = (1 << 21)-1
        else:
            global_set = 0
    else:
        value = int(calculation[1]) - 1
        if calculation[0][0] == 'a':
            global_set = global_set | (1 << value)
        elif calculation[0][0] == 'c':
            if global_set & (1 << value):
                print(1)
            else:
                print(0)
        elif calculation[0][0] == 'r':
            mask = 1 << value
            global_set = global_set & (~mask)
        elif calculation[0][0] == 't':
            global_set = global_set ^ (1 << value)


