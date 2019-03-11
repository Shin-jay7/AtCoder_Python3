# Task: https://atcoder.jp/contests/abc113/tasks/abc113_c

I = lambda: list(map(int,input().split()[::-1]))
m,n = I()

city_in_pref = [0] * (n+1) # n: num of prefs
code_list = [0] * m # m: num of cities

# Preserve input (& print) order by adding index to year & pref list
for y, p, i in sorted(I()+[i] for i in range(m)): # sorted by year
  city_in_pref[p] += 1 # Count num of cities for each pref
  code_list[i] = '%06d%06d' % (p, city_in_pref[p])

print('\n'.join(code_list))
