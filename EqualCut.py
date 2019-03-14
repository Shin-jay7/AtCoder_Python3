# Task: https://atcoder.jp/contests/abc102/tasks/arc100_b

# Cut sequence A at left, middle, right point and create B, C, D, E.
# Fix middle point and search for the best left point candidate.
# Set left point where you minimize diff between sum(B) and sum(C).
# Continue the same process for right point.
# Now you can minimize abs diff between sum(B), sum(C), sum(D) and sum(E).
# Try entire process for all middle point candidates, and find the best answer.

from itertools import accumulate

_ = input()
acc = list(accumulate(map(int, input().split())))
l,r = 0,2
total = acc[-1]
diff = total

for a in acc[1:-2]:
    while total+a > acc[r]+acc[r+1]:
        r += 1
    while a > acc[l]+acc[l+1]:
        l += 1
    sub_diff = sorted([acc[l], a-acc[l], acc[r]-a, total-acc[r]])
    diff = min(diff, sub_diff[-1]-sub_diff[0])

print(diff)
