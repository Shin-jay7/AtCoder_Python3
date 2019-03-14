# Task: https://atcoder.jp/contests/abc102/tasks/arc100_a

# Set Bi = Ai - i
# Minimize sum of abs(Bi - b)
# Bi's median is the best candidate for b
N = int(input())
nums = sorted(n-(i+1) for i,n in enumerate(map(int, input().split())))
median = nums[N//2]
print(sum(abs(n-median) for n in nums))
