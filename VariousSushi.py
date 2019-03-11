# Task: https://atcoder.jp/contests/abc116/tasks/abc116_d

N, K = list(map(int, input().split()))
t_d_pairs = [tuple(map(int, input().split())) for _ in range(N)]
t_d_pairs.sort(key=lambda x: -x[1])

d_point=0
t_set = set()
d_list = []

for t, d in t_d_pairs[:K]:
    d_point += d
    # Create d_point list for duplicated taste.
    # Note this list is in descending order.
    if t in t_set:
        d_list.append(d)
    t_set.add(t)

score = d_point + len(t_set)**2

d_smallest = d_list.pop()

# Search for other candidates in the remaining sushi.
# A new taste generates higher len(t_set)**2,
# which could metigate its lower d_score.
for t, d in t_d_pairs[K:]:
    if 0 >= len(d_list):
        break
    if t in t_set:
        continue
    t_set.add(t)
    d_point = d_point - d_smallest + d
    alt_score = d_point + len(t_set)**2
    score = max(score, alt_score)

print(score)
