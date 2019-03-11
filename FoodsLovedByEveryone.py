#Task: https://atcoder.jp/contests/abc118/tasks/abc118_b

n, m = map(int, input().split())
s = set(range(1, m+1))
for _ in range(n):
    k, *love = map(int, input().split())
    s &= set(love)
print(len(s))
