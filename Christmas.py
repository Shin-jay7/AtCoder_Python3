# Task: https://atcoder.jp/contests/abc115/tasks/abc115_d

N, X = map(int, input().split())

# Burger: bun + patty
def patty(n):
    return 2**(n+1) - 1

eaten_patty = 0

for level in range(N+1)[::-1]:
    mark = patty(level)
    # Level[N]:  B + L[N-1: patty+bun] + P + L[N-1: patty+bun] + B
    # bun == patty-1 for any level
    # Level[N]:  B + L[N-1: patty+(patty-1)] + P + L[N-1: patty+bun] + B
    # X == mark: B + L[N-1: patty+(patty-1)] + P
    if X >= mark:
        eaten_patty += patty(level-1) + 1
        X -= mark
    else:
        X -= 1

print(eaten_patty)
