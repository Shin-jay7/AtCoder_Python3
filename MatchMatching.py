#Task: https://atcoder.jp/contests/abc118/tasks/abc118_d

N, M = map(int, input().split())
nums = list(map(int, input().split()))
match_list = [0,2,5,5,4,5,6,3,7,6]

matches = []
for n in nums:
  matches += [match_list[n]]
matches.sort()

max_digits = [0]+ [-float("INF")]*N

# Max digits by i matches
for i in range(1, N+1):
  for m in matches:
    if i < m:
      continue
    elif max_digits[i-m] >= 0:
      max_digits[i] = max_digits[i-m] + 1
      break

# Qualified digit: max_digits[-1]=max_digits[N]
# Does i work for the current digit? :
# n in nums && max_digits[N- match_list[n]] = max_digits[N] - 1
nums.sort(reverse=True)
ans = []
for _ in range(max_digits[N], 0, -1):
  for n in nums:
    if N - match_list[n] < 0:
        continue
    elif max_digits[N-match_list[n]] == max_digits[N] - 1:
        N -= match_list[n]
        ans += [n]
        break

print(''.join(map(str, ans)))
