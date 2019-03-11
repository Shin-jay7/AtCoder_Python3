# Task: https://atcoder.jp/contests/abc108/tasks/arc102_a

# As (a+b)%K = 0, (a+c)%K = 0
# (a+b)%K = (a+c)%K
# b%K = c%K
# If you continue the same process for b,c and c,a combination,
# a%K = b%K = c%K
#
# In case K is odd number, a%K = b%K = c%K sould be zero.
# In case K is even number, a%K = b%K = c%K sould be zero,
#                        or a%K = b%K = c%K sould be K/2
#
# X = how many modK=0 you have in [1,2..N].
# All the possible combination for three numbers is X**3

N,K = map(int, input().split())
print((N//K)**3 + [((N+K//2)//K)**3, 0][K%2])
# or print((N//K)**3 + [((N-K//2)//K + 1)**3, 0][K%2])
