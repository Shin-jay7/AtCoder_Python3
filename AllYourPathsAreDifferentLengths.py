# Task: https://atcoder.jp/contests/abc108/tasks/arc102_b

# 2 <= L <= 10**6
# 2**20 = 1,048,576 > 10**6

# L=2**3-1 is L=111 in bainary number.
# Choose 0 or 1 for each digit.
#
# Vertex 1->2: set length 0 and 2**0 edges
# Vertex 2->3: set length 0 and 2**1 edges
# Vertex 3->4: set length 0 and 2**2 edges
#
# Now you have 000~111 ?????
#
# Reference:
# https://www.hamayanhamayan.com/entry/2018/09/02/234724
# https://creep06.hatenablog.com/entry/20180902/1535844729
# https://minus9d.hatenablog.com/entry/2018/09/02/004610

L = int(input())
B = bin(L)
N = len(B)-2

print(N, 2*N + B.count("1") - 3)

for i in range(1,N):
    print(i,i+1,0)
    print(i,i+1,2**(i-1))
    if int(B[N+2-i]):
        print(i,N,L-2**(i-1))
        L -= 2**(i-1)
