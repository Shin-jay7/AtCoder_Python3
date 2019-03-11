# Task: https://atcoder.jp/contests/abc109/tasks/abc109_b
N = int(input())
words = [input() for _ in range(N)]
print("Yes" if all(i[-1] == j[0] for i,j in zip(words, words[1:])) and len(set(words)) == N else "No")
