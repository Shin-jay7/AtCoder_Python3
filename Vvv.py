# Task: https://beta.atcoder.jp/contests/abc111/tasks/arc103_a

from collections import*
n = int(input())
v = list(map(int, input().split()))
a,b = [Counter(i).most_common()+[(0,0)] for i in (v[::2],v[1::2])]
# v: [3,1,3,2]
# a: [(3,2), (0,0)]
# b: [(1,1), (2,1), (0,0)]
i,j = a[0][1], b[0][1]
print(min(n-i-b[1][1],n-a[1][1]-j)*(a[0][0]==b[0][0]) or n-i-j)
