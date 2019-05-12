# task: https://atcoder.jp/contests/abc099/tasks/abc099_b
a,b = map(int, input().split())
n = b-a
print((n*(n+1)//2-b))
