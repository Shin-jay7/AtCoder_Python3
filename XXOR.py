#Task: https://atcoder.jp/contests/abc117/tasks/abc117_d

_, K = map(int, input().split())
A = list(map(int, input().split()))
total=max_=0
for k in range(0,K+1):
    for a in A:
        total += k ^ a
    max_ = max(max_, total)
    total = 0
print(max_)
