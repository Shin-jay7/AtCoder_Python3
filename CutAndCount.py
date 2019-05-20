# Task: https://atcoder.jp/contests/abc098/tasks/abc098_b

N = int(input())
S = input()

print(max(len(set(S[:i])&set(S[i:])) for i in range(N)))
