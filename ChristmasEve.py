# Task: https://atcoder.jp/contests/abc115/tasks/abc115_c

N, K = map(int, input().split())
trees = sorted(int(input()) for _ in range(N))[::-1]

print(min(high-low for high,low in zip(trees, trees[K-1:])))
