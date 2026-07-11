from collections import Counter


def get_pair_freqs(word_freqs: dict) -> Counter:
    pair_freqs = Counter()
    for word, freq in word_freqs.items():
        for pair in zip(word, word[1:]):
            pair_freqs[pair] += freq
    return pair_freqs

print(get_pair_freqs({('м', 'а', 'м', 'а'): 2, ('м', 'ы', 'л', 'а'): 1, ('р', 'а', 'м', 'у'): 1}))