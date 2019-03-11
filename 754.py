# Task: https://atcoder.jp/contests/abc114/tasks/abc114_b

S = input()
print(min(abs(int(S[i:i+3]) - 753) for i in range(len(S))))
