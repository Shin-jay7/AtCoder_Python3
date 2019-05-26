# Task: https://atcoder.jp/contests/abc097/tasks/arc097_b
I = lambda: list(map(int, input().split()))
n,m = I()
perm = I()
table = [_ for _ in range(n+1)]

def root(x):
    if table[x] != x:
        table[x] = root(table[x])
    return table[x]

for _ in [0]*m:
    x,y = I()
    table[root(x)] = root(y)

print(sum(root(i)==root(j) for i,j in enumerate(perm,1)))

# class UnionFind:
#     def __init__(self, n):
#         self.table = [-1]*n

#     def _root(self, x):
#         if self.table[x] < 0:
#             return x
#         else:
#             self.table[x] = self._root(self.table[x])
#             return self.table[x]

#     def find(self, x, y):
#         return self._root(x) == self._root(y)

#     def union(self, x, y):
#         r1 = self._root(x)
#         r2 = self._root(y)
#         if r1 == r2:
#             return
#         d1 = self.table[r1]
#         d2 = self.table[r2]
#         if d1 <= d2:
#             self.table[r2] = r1
#             if d1 == d2:
#                 self.table[r1] -= 1
#         else:
#             self.table[r1] = r2

# I = lambda: list(map(int, input().split()))
# n, m = I()
# ppp = I()
# uft = UnionFind(n)

# for _ in range(m):
#     x, y = I()
#     x -= 1
#     y -= 1
#     uft.union(x, y)

# ans = 0
# for i, x in enumerate(ppp):
#     if uft.find(i, x-1):
#         ans += 1

# print(ans)
