# Task: https://atcoder.jp/contests/abc106/tasks/abc106_d

# # Solution 1
_,M,Q = map(int, input().split())
sections = [list(map(int, input().split())) for _ in range(M)]
queries = [list(map(int, input().split())) for _ in range(Q)]

for q in queries:
    count = 0
    for s in sections:
        if q[0]<=s[0] and s[1]<=q[1]:
            count += 1
    print(count)

# Solution 2
# Train moves from left to right,
# so you can consider this as left-right 2 dimension matrix

# import numpy as np
# N, M, Q = map(int, input().split())

# train = np.zeros((N, N))
# for _ in range(M):
#     L, R = map(int, input().split())
#     train[N-L][R-1] += 1
#     # Plot train data onto this matrix style,
#     # and cumulative sum works well to get answer.
# train = np.cumsum(np.cumsum(train, axis=0), axis=1)

# for _ in range(Q):
#     p, q = map(int, input().split())
#     print(int(train[N-p][q-1]))

# Solution 3
# Non Numpy version

# N,M,Q = map(int, input().split())
# train = [[0 for _ in range(N)] for _ in range(N)]

# for _ in range(M):
#     L,R = map(int, input().split())
#     train[N-L][R-1] += 1

# for l in range(N): # Cumulative sum across horizontal axis
#     for r in range(1,N):
#         train[l][r] += train[l][r-1]

# for l in range(1,N): # Cumulative sum across vertical axis
#     for r in range(N):
#         train[l][r] += train[l-1][r]

# for _ in range(Q):
#     l,r = map(int, input().split())
#     print(train[N-l][r-1])
