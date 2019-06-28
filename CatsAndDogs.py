# Task: https://atcoder.jp/contests/abc094/tasks/abc094_a

A,B,X = map(int, input().split())
print(["No","YES"][~B<A-X<1])
