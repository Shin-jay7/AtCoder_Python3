# Task: https://atcoder.jp/contests/abc107/tasks/arc101_b

# N = int(input())
# A = list(map(int, input().split()))
# M = []

# if N == 1:
#     print(*A)
# else:
#     for i in range(N-1):
#         for j in range(i+1,N):
#             M.append(A[(j-i+1)//2])
#     M.sort()
#     print(mid[len(M)//2])

# Subsequence combination for A: N x (N+1) / 2
# Binary search:
# In all the subsequence combination, half of numbers
# should be equal or larger than Median of Medians.
# Set "equal or larger than MoM" as +1 and
# "smaller than MoM" as -1, total should be 0 or higher.

N = int(input())
nums = list(map(int, input().split()))

def check(x):
    counter = [0]*(2*N+1)
    index = N
    count = 0
    subsequences = 0
    for i in range(N):
        counter[index] += 1
        if nums[i] < x:
            count += counter[index]
            index += 1
        else:
            index -= 1
            count -= counter[index]
        subsequences += count
    return subsequences

sorted_nums = sorted(nums)
left, mid, right = 0, N//2, N
total = N*(N+1)//2

while True:
    if check(sorted_nums[mid]) <= total//2:
        if mid == N-1:
            break
        elif check(sorted_nums[mid+1]) > total//2:
            break
        else:
            left, mid = mid, (mid+right)//2
    else:
        mid, right = (mid+left)//2, mid+1

print(sorted_nums[mid])
