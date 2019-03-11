# Task: https://atcoder.jp/contests/abc112/tasks/abc112_c

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
x,y,h = points[0]
for X in range(101):
    for Y in range(101):
        H = h+abs(X-x)+abs(Y-y)
        if all(max(H-abs(X-_[0])-abs(Y-_[1]), 0) == _[2] for _ in points):
            print(X,Y,H)
