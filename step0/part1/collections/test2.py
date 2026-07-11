from collections import Counter


word = ['м', 'а', 'м', 'а']
pairs = Counter()
for i in range(len(word) - 1):
    pair = word[i] + word[i + 1]
    pairs[pair] += 1

print(pairs)