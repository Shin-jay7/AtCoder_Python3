# Task: https://atcoder.jp/contests/abc118/tasks/abc118_a?lang=en

A, B = map(int, input().split())
print(A+B if B%A == 0 else B-A)
