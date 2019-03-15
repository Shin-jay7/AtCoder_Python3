# Task: https://atcoder.jp/contests/abc101/tasks/arc099_a

# N: Number of sequences
# K: Length of covering arrow (= Take K digits in the sequence)
# X: Covered area by arrows
# G: Number of arrows

# Set the first K including "1" (G = 1)
# Cover the remaining area by G-1 times of K-1
# X = K + (G-1)(K-1)
# N <= X = K + (G-1)(K-1)
# N <= K + (G-1)(K-1)
# G >= (N-1)/(K-1)
# Find minimum G satisfing the above condition
# G = ceiling((N-1)/(K-1))
# Note ceiling x//y is (x-1)//y + 1 (Note ceiling x/y is (x+y-1)/y)
# G = ((N-1)-1))//(K-1) + 1
# G = (N-2)//(K-1) + 1

N,K = map(int, input().split())
print((N-2)//(K-1) + 1)
