# Task: https://atcoder.jp/contests/abc105/tasks/abc105_b
N = int(input())
print("Yes" if N >= 7*((-N)%4) else "No")
