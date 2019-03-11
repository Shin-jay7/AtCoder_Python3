# Task: https://atcoder.jp/contests/abc113/tasks/abc113_d

# Dynamic programming: https://en.wikipedia.org/wiki/Dynamic_programming

# H: height: H+1cm
# W: num of vertical lines
# K: goal: Kth vertical line

# Position: P(h, w)
# P(h, w) moves down to P(h+1, w-1) or P(h+1, w) or P(h+1, w+1)
# X: num of path to P(h+1, w-1)
# Y: num of path to P(h+1, w)
# Z: num of path to P(h+1, w+1)
# X + Y + Z  = ?

# W vertical lines == W-1 space between lines
# Set "1" if you put horizonal line in the space, else set "0"
# Possible patterns: 2**(W-1)
# Caveat: Do not set "1" before or after "1" (Amidakuji rule!)
# Example: Good)    "1001001"
# Example: No good) "1001101"

# 1 or 2 vertical lines you have 1 Amidakuji pattern.
# Vertical lines: 1, 2, 3,...W-2, W-1, W
# F(W): How many horizontal lines you can put between 1 to W?
# If you do not put horizontal line between W and W-1, you have F(W-1) pattern.
# If you put horizontal line between W and W-1,
#    you are not allowed to set horizontal line between W-1 and W-2 (Amidakuji rule!),
#    now you have F(W-2)
# F(W) = F(W-1) + F(W-2)
# Fibonacci sequence!!!!!

H, W, K = map(int, input().split())
f = [1, 1, 2, 3, 5, 8, 13, 21]
Q = 10**9 + 7

dp = [[1]+[0]*(W-1) for _ in range(H+1)]
# # if H = W = 3
# # dp[
# #    [1, 0, 0],
# #    [1, 0, 0],
# #    [1, 0, 0],
# #    [1, 0, 0]
# # ]

if W == 1:
    H = 0
for i in range(1,H+1): # アミダ（dp)は0行目からスタートするが、確率計算するのは1行目から
                       # 常に一つ上の行の確率を足すので、0行目がないと１行目の計算で詰まる
    for j in range(W): # Fibonacciとindexを合わせてる
        if j == 0: # First vertical line: 真上と右上の確率を足す
            dp[i][0] = (dp[i-1][0]*f[W-1] + dp[i-1][1]*f[W-2])%Q
        elif j == W-1: # Last vertical line: F(W) = F(W-1) + F(W-2) 真上と左上の確率を足す
            dp[i][W-1] = (dp[i-1][W-1]*f[W-1] + dp[i-1][W-2]*f[W-2])%Q
        else: # Middle vertical lines:
              # Amidakuji comes down to dp[i][j] from three position at one level above
              # 真上、左上、右上の確率を足す
            dp[i][j] = (dp[i-1][j]*f[j]*f[W-j-1] + dp[i-1][j-1]*f[j-1]*f[W-j-1] + dp[i-1][j+1]*f[j]*f[W-j-2])%Q
# # dp[
# #    [1, 0, 0],
# #    [2, 1, 0],
# #    [5, 3, 1],
# #    [13, 9, 5]
# #              ]
print(dp[H][K-1])

