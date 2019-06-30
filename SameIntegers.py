# Task: https://atcoder.jp/contests/abc093/tasks/arc094_a
_min,_mid,_max = sorted(map(int, input().split()))
print(_max-_mid+(_mid-_min+1)//2+(_mid-_min&1))
