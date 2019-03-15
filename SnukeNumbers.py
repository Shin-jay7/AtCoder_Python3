# Task: https://atcoder.jp/contests/abc101/tasks/arc099_b

# I ahve no idea why Snuke numbers more than 10 always holds
# 9 in most (but not all) of last digits....
t=i=1
K = int(input())

while K:
    if t < i / sum(map(int, list(str(i)))):
        i += 9*t
        t *= 10
    else:
        print(i)
        i += t
        K -= 1
