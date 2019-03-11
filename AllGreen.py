# Task: https://atcoder.jp/contests/abc104/tasks/abc104_c

# For each question:
#     1) Solve all sub questions
#     2) Solve no sub question
# Then, if necessary,
# 3) solve 1 ~ all but one sub questions for the highest
#    score question in the remaining option.
# If you do not exceed the target score, your choice on 1) was wrong.

# https://www.tatsumiya-blog.tokyo/entry/competitive-programming/abc-104#C-All-Green

D,G = map(int, input().split())
PC = [0]+[list(map(int, input().split())) for _ in range(D)]

# ?????
def f(p,c):
    if p == 0:
        return 10**9
    m = min(c//(p*100), PC[p][0])
    s = 100*p*m
    if m == PC[p][0]:
        s += PC[p][1]
    if s < c:
        m += f(p-1,c-s)
    return min(m,f(p-1,c))

print(f(D,G))
