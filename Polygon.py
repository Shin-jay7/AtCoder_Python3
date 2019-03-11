#Task: https://atcoder.jp/contests/abc117/tasks/abc117_b

_ = input()
n = list(map(int, input().split()))
print(["No", "Yes"][sum(n)>max(n)*2])
