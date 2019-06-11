# Task: https://atcoder.jp/contests/abc095/tasks/arc096_a
A,B,C,X,Y = map(int, input().split())

print(min(X*A+Y*B, 2*X*C+B*max(0,Y-X), 2*Y*C+A*max(0,X-Y)))
