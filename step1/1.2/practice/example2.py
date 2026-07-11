from itertools import pairwise
from collections import Counter

def get_pair_freqs(word_freqs: dict) -> Counter:
    pair_freqs = Counter()
    for word, freq in word_freqs.items():
        for pair in pairwise(word):
            pair_freqs[pair] += freq
    return pair_freqs

print(get_pair_freqs({('м', 'а', 'м', 'а'): 2, ('м', 'ы', 'л', 'а'): 1, ('р', 'а', 'м', 'у'): 1}))
# Counter({('м', 'а'): 4, ('а', 'м'): 3, ('м', 'ы'): 1, ('ы', 'л'): 1, ('л', 'а'): 1, ('р', 'а'): 1, ('м', 'у'): 1})