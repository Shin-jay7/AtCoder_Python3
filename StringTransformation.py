# Task: https://atcoder.jp/contests/abc110/tasks/abc110_c

from collections import Counter as C
print(["No","Yes"][C(C(input()).values()) == C(C(input()).values())])
# 'apple'
# C(input()): Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})
# C(input()).values(): dict_values([1, 2, 1, 1])
# C(C(input()).values()): Counter({1: 3, 2: 1})
