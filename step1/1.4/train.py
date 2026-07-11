from itertools import pairwise
from collections import Counter

def merge_pair(pair: tuple[str, str], word_freqs: dict[tuple[str, ...], int]) -> dict[tuple[str, ...], int]:
    """Замена всех pair на объединённый токен во всех словах word_freqs."""
    new_word_freqs = {}
    merged_token = pair[0] + pair[1]
    
    for word, freq in word_freqs.items():
        new_word = []
        i = 0
        # Сокращаем цикл через while + срезы вместо индексации
        while i < len(word):
            if word[i:i+2] == pair:  # Сравнение среза вместо двух индексов
                new_word.append(merged_token)
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        
        new_word_freqs[tuple(new_word)] = freq  
    
    return new_word_freqs

def get_word_freqs(text: str) -> dict[tuple[str, ...], int]:
    """Возвращает словарь частот слов в виде кортежей символов."""
    words = text.split()
    words_tuples = [tuple(word) for word in words]
    return dict(Counter(words_tuples))

def get_pair_freqs(word_freqs: dict) -> Counter:
    pair_freqs = Counter()
    for word, freq in word_freqs.items():
        for pair in pairwise(word):
            pair_freqs[pair] += freq
    return pair_freqs

def get_alphabet(word_freqs: dict) -> set[str]:
    """Возвращает множество уникальных символов (алфавит) из словаря word_freqs."""
    alphabet = set()
    for word in word_freqs.keys():
        alphabet.update(word)
    return alphabet

def train(text: str, vocab_size: int) -> tuple[list[tuple[str, str]], dict[tuple[str, ...], int]]:
    """Обучение модели BPE на основе текста и желаемого размера словаря."""
    word_freqs = get_word_freqs(text)
    merges = []  # список пар в порядке их слияния

    num_merges = vocab_size - len(get_alphabet(word_freqs))
    
    for step in range(num_merges):
        pair_freqs = get_pair_freqs(word_freqs)
        if not pair_freqs:
            break
        best_pair = max(pair_freqs, key=pair_freqs.get)
        word_freqs = merge_pair(best_pair, word_freqs)
        merges.append(best_pair)

    return merges, word_freqs 

print(train("Искусственный интеллект и машинное обучение навсегда изменили наш мир. Современные нейронные сети умеют читать книги, писать сложные стихи и сочинять красивую музыку. Большие языковые модели, такие как трансформеры, ежедневно обрабатывают огромные массивы текстов. Они аккуратно разбивают слова на маленькие токены, вычисляют их математические вероятности и пытаются предсказать каждое следующее слово.", 50))

