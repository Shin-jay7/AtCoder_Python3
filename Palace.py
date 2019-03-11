# Task: https://atcoder.jp/contests/abc113/tasks/abc113_b

_ = input()
T, A = map(int, input().split())
H = [abs(T - 0.006*height - A) for height in map(int, input().split())]

print(H.index(min(H))+1)
