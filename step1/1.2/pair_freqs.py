from collections import Counter


def get_pair_freqs(word_freqs: dict) -> Counter:
    pair_freqs = Counter()
    for word, freq in word_freqs.items():
        for pair in zip(word, word[1:]):
            pair_freqs[pair] += freq
    return pair_freqs