# https://atcoder.jp/contests/abc115/tasks/abc115_b

N = int(input())
price_list = sorted(int(input()) for _ in range(N))[::-1]

print(sum(price_list) - max(price_list)//2)
