#Task: https://atcoder.jp/contests/abc118/tasks/abc118_c

n = int(input())
mons = [int(_) for _ in input().split()]

def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x

ans = mons[0]
for mon in mons:
    ans = gcd(ans, mon)

print(ans)
