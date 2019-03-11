# Task: https://atcoder.jp/contests/abc109/tasks/abc109_d

# Move: (1,1)->(1,2)...->(1,W)->(2,W)->(2,W-1)...
#       ->(2,2)->(2,1)->(3,1)->(3,2)...
# If you find odd number,
#     subtract 1 from the column and add 1 onto the next column.

H,W = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]
ops = []

for i in range(H):
    # Move 1 to the right next column
    for j in range(W-1):
        if matrix[i][j]%2:
            matrix[i][j+1] += 1
            # Notice this matrix starts at (1,1) in task definition,
            # but index begins at (0,0), so needs +1 for each coordinates.
            ops.append([i+1,j+1,i+1,j+2])
    # Move 1 to the downward next column
    if i < H-1 and matrix[i][W-1]%2:
        matrix[i+1][W-1] += 1
        ops.append([i+1,W,i+2,W])

print(len(ops))
for op in ops:
    print(*op)
