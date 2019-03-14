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
l,r = 0,2 # left: l, middle: m, right: r
total = acc[-1]
diff = total

for m in acc[1:-2]:
    while total+m > acc[r]+acc[r+1]:
        r += 1
    while m > acc[l]+acc[l+1]:
        l += 1
    sub_diff = sorted([acc[l], m-acc[l], acc[r]-m, total-acc[r]])
    diff = min(diff, sub_diff[-1]-sub_diff[0])

print(diff)
