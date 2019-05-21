# Task: https://atcoder.jp/contests/abc098/tasks/arc098_b
_ = input()
N = list(map(int, input().split()))
xor_=sum_=l=ans=0

for r,n in enumerate(N):
    xor_ ^= n
    sum_ += n
    while xor_ < sum_:
        xor_ ^= N[l]
        sum_ -= N[l]
        l += 1
    ans += r-l+1

print(ans)
