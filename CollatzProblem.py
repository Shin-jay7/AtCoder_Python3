#Task: https://atcoder.jp/contests/abc116/tasks/abc116_b

s = int(input())
i = 4
while s not in [1,2,4]:
    s = [s//2, s*3+1][s%2]
    i+=1
print(i)
