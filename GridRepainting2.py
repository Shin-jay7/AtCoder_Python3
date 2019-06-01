# Task: https://atcoder.jp/contests/abc096/tasks/abc096_c
H,W = map(int, input().split())
grid = [input() for _ in range(H)]
ans = 'Yes'

for i in range(1,H-1):
    for j in range(1,W-1):
        if grid[i][j] == '#':
            if grid[i-1][j]==grid[i+1][j]==grid[i][j-1]==grid[i][j+1]=='.':
                ans = 'No'
print(ans)
