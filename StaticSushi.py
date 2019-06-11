# Task: https://atcoder.jp/contests/abc095/tasks/arc096_b
from itertools import accumulate

N,C = map(int, input().split())
X,V = [],[]
for _ in range(N):
    x,v = map(int, input().split())
    X.append(x)
    V.append(v)

V_ret,X_ret = V[::-1],X[::-1]
S,S_ret = list(accumulate(V)), list(accumulate(V_ret))

S[0] -= X[0]
S_ret[0] -= (C-X_ret[0])

for i in range(1,N):
    S[i] = max(S[i-1], S[i]-X[i])
    S_ret[i] = max(S_ret[i-1], S_ret[i]-(C-X_ret[i]))

ans = max(0, max(S), max(S_ret))

for i in range(N-1):
    tmp1 = S[i]+S_ret[N-(i+2)]-X[i]
    tmp2 = S_ret[i]+S[N-(i+2)]-(C-X_ret[i])
    ans = max(ans, tmp1, tmp2)

print(ans)
