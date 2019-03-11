# Task: https://atcoder.jp/contests/abc105/tasks/abc105_c
N = int(input())
S = ""

while N:
    S = str(N%2) + S
    N = -(N//2)

print(S if S else 0)
