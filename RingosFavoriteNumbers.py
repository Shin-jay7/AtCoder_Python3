# Task: https://atcoder.jp/contests/abc100/tasks/abc100_b
D, N = map(int, input().split())
if N == 100:
    N += 1
print(N*100**D)
