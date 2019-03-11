# Task: https://atcoder.jp/contests/abc106/tasks/abc106_c
# "1"->"1"->"1"...->"1"
# "2"->"22"->"2222"...->"2...(continue 5 x 10**15 times)"
# "3"->...............->"3...(continue 5 x 10**15 times)"
# 2 or larger number generates almost infinite digits in 5 x 10**15 days.

for i in list(input()):
    if i != '1':
        break
_ = input()
print(i)
