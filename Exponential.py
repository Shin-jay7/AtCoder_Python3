# Task: https://atcoder.jp/contests/abc097/tasks/abc097_b
X = int(input())
r=range(1,32)

print(max(b**p*(b**p<=X) for p in r[1:] for b in r))
