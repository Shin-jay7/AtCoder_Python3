# Task: https://atcoder.jp/contests/abc101/tasks/abc101_b
N = input()
print(["Yes","No"][int(N)%sum(map(int, N))])
