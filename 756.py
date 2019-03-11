#Task: https://atcoder.jp/contests/abc114/tasks/abc114_d

# 32400: 2**4 x 3**4 x 5**2
# divisors for 32400: 2**a x 3**b x 5**c
#                     a: 0,1,2,3,4
#                     b: 0,1,2,3,4
#                     c: 0,1,2
#                     5 x 5 x 3 = 75 patterns

# Possible combination for 75 divisors
#  p**4 x q**4 x r**2
#  p**14 x q**4
#  p**24 x q**2
#  p**74

# e(s): exponential num for s at N! prime factorization
# e(p) >= 4, e(q) >= 4, e(r) >= 2
# p**4 x q**4 x r**2 is divisor for N!

N = int(input())

# Count exponential num for divisors at N! factorization
e = [0] * (N+1)
for i in range(2, N+1):
    cur = i
    for j in range(2, i+1):
        while cur%j == 0:
            e[j] += 1
            cur //= j

# Number of e elements, equal to or larger than n-1
def f(n):
    return len(list(filter(lambda x: x >= n-1, e)))

# # n: possible combination for 75 divisors
print(f(75)
    + f(15) * (f(5)-1)
    + f(25) * (f(3)-1)
    + f(5) * (f(5)-1) * (f(3)-2) // 2)
