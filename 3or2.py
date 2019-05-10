# Task: https://atcoder.jp/contests/abc100/tasks/abc100_c
_ = input()
nums = map(int, input().split())
print(sum(bin(n)[::-1].index('1') for n in nums))
