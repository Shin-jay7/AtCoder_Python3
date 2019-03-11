# Task: https://atcoder.jp/contests/abc103/tasks/abc103_c

# Set M = a1 x a2 x...x aN
# M mod ai = 0
# (M-1) mod = ai-1
# f(M-1) = (a1-1) + (a2-1) +...+(aN-1)
N = int(input())
print(sum(map(int, input().split()))-N)
