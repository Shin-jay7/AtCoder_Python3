# Task: https://atcoder.jp/contests/abc108/tasks/abc108_b
x1,y1,x2,y2 = map(int, input().split())
x_diff = x2-x1
y_diff = y2-y1
print(x2-y_diff, y2+x_diff, x1-y_diff, y1+x_diff)
