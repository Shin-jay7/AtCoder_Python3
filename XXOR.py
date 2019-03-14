#Task: https://atcoder.jp/contests/abc117/tasks/abc117_d

_, K = map(int, input().split())
A = list(map(int, input().split()))
max_=0
for k in range(K+1):
    total = 0
    for a in A:
        total += k ^ a
    max_ = max(max_, total)
print(max_)
