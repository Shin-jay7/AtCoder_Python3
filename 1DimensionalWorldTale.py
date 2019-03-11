# Task: https://atcoder.jp/contests/abc110/tasks/abc110_b

I = lambda: map(int, input().split())
N,M,X,Y = I()
print("No War" if max(list(I())+[X]) < min(list(I())+[Y]) else "War")
