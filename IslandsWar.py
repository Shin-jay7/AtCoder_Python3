# Task: https://atcoder.jp/contests/abc103/tasks/abc103_d

# Sort (ai, bi) list by bi
# 1) If the request (ai, bi) has already been satisfied,
#    which means the bridge x was removed at the previous request
#    (ai <= x ), do nothing.
# 2) If the request (ai, bi) has not been satisfied (ai > x),
#    cut off bi-1 bridge between bi-1 and bi islands.

N,M = map(int, input().split())
ab = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda ab: ab[1])
x=cnt=0

for (a,b) in ab:
    if a > x:
        x = b-1
        cnt += 1

print(cnt)
