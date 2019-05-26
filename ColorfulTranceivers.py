# Task: https://atcoder.jp/contests/abc097/tasks/abc097_a
a,b,c,d = map(int, input().split())
print(["No","Yes"][abs(a-c)<=d or abs(a-b)<=d and abs(b-c)<=d])
# print('YNeos'[input()[-1]in'29'::2])
