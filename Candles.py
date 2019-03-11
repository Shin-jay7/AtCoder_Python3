# Task: https://atcoder.jp/contests/abc107/tasks/arc101_a
_,K = map(int, input().split())
X = list(map(int, input().split()))
# Find K continuous candles with shortest distance
# between the first and last candle.
# Compare which is shorter:
#        first->last or last->first
#        |first| + |last-first|  or  |last| + |last-first|
min_ = min(b - a + min(abs(a), abs(b)) for a,b in zip(X, X[K-1:]))
print(min_)
