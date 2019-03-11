#Task: https://atcoder.jp/contests/abc117/tasks/abc117_c

N, _ = map(int, input().split())
target = sorted(map(int, input().split()))
# Discending sort by target-target distances
distance = sorted(j-i for i, j in zip(target, target[1:]))[::-1]
# Put N on targets by discending distance order
print(sum(distance[N-1:]))
