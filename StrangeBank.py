# task: https://atcoder.jp/contests/abc099/tasks/abc099_c
from itertools import count, takewhile

def dfs(n, d={}):
    if n < 6:
        return n

    if n in d:
        return d[n]

    max9 = max(takewhile(lambda x: x<=n, (9**i for i in count())))
    max6 = max(takewhile(lambda x: x<=n, (6**i for i in count())))
    d[n] = min(dfs(n-max9), dfs(n-max6)) + 1

    return d[n]

print(dfs(int(input())))
