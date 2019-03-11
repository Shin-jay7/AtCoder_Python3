# Task: https://atcoder.jp/contests/abc114/tasks/abc114_c

n = int(input())

def three_five_seven_generator(str):
  # 3. Iteration stops if str reaches the input number.
  if int(str) > n:
    return 0
  # 2. True if str includes all of '3' and '5' and '7'
  count = 1 if all( _ in str for _ in '357') else 0
  # 1. Generate numbers with '3' or/and '5' or/and '7' such as
  #    '03', '05', '07', '033', '035', '037', '053', '055', '057'..
  for _ in '357':
    count += three_five_seven_generator(str + _)
  return count

  # 4. This generator does not start at '',
  #    but '0' in order to avoid error at line 7.
print(three_five_seven_generator('0'))
