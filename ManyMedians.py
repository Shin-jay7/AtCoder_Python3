# Task: https://atcoder.jp/contests/abc094/tasks/arc095_a
N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)[N//2-1:N//2+1]

for x in X:
    print(Y[x<=Y[0]])
