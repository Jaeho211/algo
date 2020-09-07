import sys
from functools import cmp_to_key

# example
# 34 45 56 12 23 30 40 10


def compare(item1, item2):
    differ = item1%10 - item2%10
    if differ != 0:
        return differ
    else:
        return item1 - item2


cake_lengths = list(map(int, sys.stdin.readline().split()))
cake_lengths.sort(key=cmp_to_key(compare))

print(cake_lengths)