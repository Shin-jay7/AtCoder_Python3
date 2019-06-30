# Task: https://atcoder.jp/contests/abc093/tasks/arc094_b
# Reference: https://misteer.hatenablog.com/entry/ARC094-D
import math
for A,B in[map(int,input().split())for _ in range(int(input()))]:
 R = int(math.sqrt(A*B))
 N = not R*(R+1)<A*B
 print(2*(R-N)-(not ((N and R*R<A*B) or A==B)))
