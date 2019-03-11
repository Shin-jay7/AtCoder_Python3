# Task: https://atcoder.jp/contests/abc112/tasks/abc112_b

I = lambda: map(int, input().split())
N, T = I()

print(min([c for c,t in [I() for _ in range(N)] if t<=T], default='TLE'))
