# Task: https://atcoder.jp/contests/abc109/tasks/abc109_c
from functools import reduce
from fractions import gcd
N,X = map(int, input().split())
x = [abs(X-int(i)) for i in input().split()]
print(reduce(gcd,x))
