# Task: https://atcoder.jp/contests/abc100/tasks/abc100_d
N,M = map(int, input().split())
cakes = [[],[],[],[],[],[],[],[]]

for _ in range(N):
    x,y,z = map(int, input().split())
    cakes[0].append(x+y+z)
    cakes[1].append(x+y-z)
    cakes[2].append(x-y+z)
    cakes[3].append(x-y-z)
    cakes[4].append(-x+y+z)
    cakes[5].append(-x+y-z)
    cakes[6].append(-x-y+z)
    cakes[7].append(-x-y-z)

for i in range(8):
    cakes[i].sort(reverse=True)

print(max([sum(cakes[i][:M]) for i in range(8)]))
