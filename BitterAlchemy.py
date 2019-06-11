# Task: https://atcoder.jp/contests/abc095/tasks/abc095_b

N,X = map(int, input().split())
m = [int(input()) for _ in range(N)]

print(N+(X-sum(m))//min(m))
