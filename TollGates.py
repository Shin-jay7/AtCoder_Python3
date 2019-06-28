# Task: https://atcoder.jp/contests/abc094/tasks/abc094_b

I = lambda: map(int, input().split())
_,m,x = I()

low = sum(i<x for i in I())
high = m-low
print(min(low,high))
