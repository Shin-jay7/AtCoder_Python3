# Task: https://atcoder.jp/contests/abc107/tasks/abc107_b

H,_ = map(int, input().split())
matrix = []

for row in [list(input()) for _ in range(H)]:
    if '#' in row:
        matrix.append(row)

matrix = zip(*[column for column in zip(*matrix) if '#' in column])

for row in matrix:
    print(*row,sep="")
