# task: https://atcoder.jp/contests/abc099/tasks/abc099_d
import itertools

N,C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
cl_cnt = [[0 for _ in range(C)] for _ in range(3)]

for i in range(N):
    ci = list(map(int, input().split()))
    for j,cij in enumerate(ci):
        cl_cnt[(i+j)%3][cij-1] += 1

cost = [[0 for _ in range(C)] for _ in range(3)]

for i in range(3):
    for j in range(C):
        for k in range(C):
            cost[i][k] += (D[j][k]) * cl_cnt[i][j]

ans = 1000*500*500

for i,j,k in itertools.permutations(range(C),3):
    ans = min(cost[0][i]+cost[1][j]+cost[2][k], ans)

print(ans)
