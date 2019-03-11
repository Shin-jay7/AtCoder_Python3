# Task: https://atcoder.jp/contests/abc110/tasks/abc110_d

import math
n,m = map(int, input().split())
mm = int(math.sqrt(m))
s = {}

for i in range(2,mm+2):
    if m%i != 0:
        continue
    while m%i == 0:
        m = m//i
        # Count each prime's exponential numbers
        # get() return a value for the given key (i).
        # If key is not available, then returns default value(0)
        s[i] = s.get(i,0) + 1
    if m == 1:
        break

if m >= 2:
    s[1] = 1
ans = 1
mod = 10**9+7

# Distribute expo nums by n-1 partitions
for i in s.values():
    # n H i = n+i-1 C i
    # (n+i-1)! / i!((n+i-1)-i)!
    for j in range(1,i+1):
        ans = ans * (n+j-1)//(j) # ?????
    # You can divide by 10**9+7 in the middle of calculation.
    ans %= mod

print(ans)
