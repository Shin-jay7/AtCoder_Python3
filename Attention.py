# Task: https://atcoder.jp/contests/abc098/tasks/arc098_a
N = int(input())
S = input()

cnt = mi= S.count("E")
for i in range(N):
    if S[i] == "W" : cnt+=1
    else : cnt-=1
    mi = min(mi,cnt)
print(mi)
