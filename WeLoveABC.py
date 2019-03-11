# Task: https://atcoder.jp/contests/abc104/tasks/abc104_d

# Reference:
# https://betrue12.hateblo.jp/entry/2018/08/05/230358

C = [1,0,0,0] # Counter for "A", "AB", "ABC"

for str in input():
    if str != "?":
        i = "ABC".find(str) # Return if str is "A" or "B" or "C" by index
        C[i+1] += C[i]
    else:
        # Three letters, "A" or "B" or "C", replaces "?"
        C = [C[0]*3, C[1]*3+C[0], C[2]*3+C[1], C[3]*3+C[2]]
    C = [_%(10**9+7) for _ in C]

print(C[3])
