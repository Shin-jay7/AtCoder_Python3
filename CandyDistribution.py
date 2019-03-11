# Task: https://atcoder.jp/contests/abc105/tasks/abc105_d

# Accumulative sum until Ai: Bi
# Al +...+ Ar = Br - B(l-1)
# Al +...+ Ar is multiple of M
# Br = multiple of M + B(l-1)
# Br and B(l-1) have the same mod M
N,M = map(int, input().split())
*A, = map(int, input().split())
# A = list(map(int, input().split()))
counter = {0: 1}
mod=total=0

for a in A:
    mod = (mod+a) % M # Calculate mod for accumlative sum
    # +1 if the acculative sum has as same mod as previous one.
    total += counter.get(mod,0)
    # Record this mod who may or may not matches with coming mods.
    counter[mod] = counter.get(mod,0) + 1

print(total)


