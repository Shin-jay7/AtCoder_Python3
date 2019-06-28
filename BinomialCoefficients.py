# Task: https://atcoder.jp/contests/abc094/tasks/arc095_b
input()
arr = sorted(list(map(int, input().split())))
m = max(arr)
print(m, min(arr,key=lambda x:abs(m-x*2)))
