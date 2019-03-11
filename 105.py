# Task: https://atcoder.jp/contests/abc106/tasks/abc106_b

# Odd numbers with 8 divisors:
# Prime factors p, q, r should be odd number.
# p**7 or p**3*q or p*q*r
N = int(input())
print(sum(i<=N for i in [105,135,165,189,195]))
