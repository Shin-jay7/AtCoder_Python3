# Task: https://atcoder.jp/contests/abc116/tasks/abc116_c

_ = input()
nums = map(int,input().split())

ans=prev=0
for n in nums:
    ans += max(n-prev,0)
    prev = n
print(ans)
