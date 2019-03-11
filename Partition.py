# Task: https://atcoder.jp/contests/abc112/tasks/abc112_d

# if D = gcd(a1,a2,...aN):
#   a1%D == 0
#   a2%D == 0
#   aN%D == 0
#
# M = a1 + a2...+aN
# M%D == 0

# a1 >= D
# a2 >= D
# ...
# aN >= D
#
# M >= N * D

def gcd():
    N, M = map(int, input().split())
    for i in range(M//N+1)[::-1]:
        if M%i==0:
            return i
print(gcd())
