# Task: https://atcoder.jp/contests/abc096/tasks/abc096_d

# Find five prime numbers, whoes mod5 = 1.
# Sum up these numbers reslut in multiple of 5.
# Same is true for mod5 = 2 (or 3, 4).

N = int(input())
ans = []
num = 6  # 5+1

while len(ans) < N:
    num += 5
    if all(num%i != 0 for i in range(2, int(num**0.5)+1)):
        ans.append(num)

print(*ans)
