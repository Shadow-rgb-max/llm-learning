from collections import Counter
from typing import Tuple

def get_word_freqs(text : str) -> dict[Tuple[str, ...], int]:
    words = text.split()
    words_tuples = [tuple(word) for word in words]
    return dict(Counter(words_tuples))

print(get_word_freqs("мама мыла раму мама"))
