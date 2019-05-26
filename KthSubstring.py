# Task: https://atcoder.jp/contests/abc097/tasks/arc097_a
s = input()
K = int(input())

print(sorted({s[i:i+j] for i in range(len(s)) for j in range(6)})[K])
