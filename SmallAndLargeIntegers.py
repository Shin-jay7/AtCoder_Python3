# Task: https://atcoder.jp/contests/abc093/tasks/abc093_b
A,B,K = map(int, input().split())
r = range(A,B+1)
ans = sorted(set(r[:K])|set(r[-K:]))
for a in ans:
    print(a)
