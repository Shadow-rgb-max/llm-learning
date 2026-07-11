from collections import Counter
from itertools import pairwise

class BPETokenizer:
    def __init__(self):
        self.merges = []  # список пар в порядке обучения

    def merge_pair_in_tokens(self, pair: tuple[str, str], tokens: list[str]) -> list[str]:
        """Заменяет все вхождения pair на объединённый токен в списке tokens."""
        merged_token = pair[0] + pair[1]
        new_tokens = []
        i = 0
        while i < len(tokens):
            if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == pair:
                new_tokens.append(merged_token)
                i += 2  # пропускаем оба символа пары
            else:
                new_tokens.append(tokens[i])
                i += 1
        return new_tokens

    def get_word_freqs(self, text: str) -> dict[tuple[str, ...], int]:
        words = text.split()
        words_tuples = [tuple(word) for word in words]
        return dict(Counter(words_tuples))
    
    def get_pair_freqs(self, word_freqs: dict) -> Counter:
        pair_freqs = Counter()
        for word, freq in word_freqs.items():
            for pair in pairwise(word):
                pair_freqs[pair] += freq
        return pair_freqs
    
    def get_alphabet(self, word_freqs: dict) -> set[str]:
        alphabet = set()
        for word in word_freqs.keys():
            alphabet.update(word)
        return alphabet
    
    def merge_pair(self, pair: tuple[str, str], word_freqs: dict[tuple[str, ...], int]) -> dict[tuple[str, ...], int]:
        new_word_freqs = {}
        merged_token = pair[0] + pair[1]
        
        for word, freq in word_freqs.items():
            new_word = []
            i = 0
            while i < len(word):
                if word[i:i+2] == pair:
                    new_word.append(merged_token)
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1
            
            new_word_freqs[tuple(new_word)] = freq  
        
        return new_word_freqs

    def train(self, text: str, vocab_size: int):
        word_freqs = self.get_word_freqs(text)
        num_merges = vocab_size - len(self.get_alphabet(word_freqs))
        if vocab_size < len(self.get_alphabet(word_freqs)):
            raise ValueError(f"vocab_size must be greater than the number of alphabet characters ({len(self.get_alphabet(word_freqs))}).")
        for _ in range(num_merges):
            pair_freqs = self.get_pair_freqs(word_freqs)
            if not pair_freqs:
                break
            best_pair = max(pair_freqs, key=pair_freqs.get)
            word_freqs = self.merge_pair(best_pair, word_freqs)
            self.merges.append(best_pair)

    def encode(self, text: str) -> list[str]:
        tokens = list(text)  # разбиваем текст на символы
        for pair in self.merges:
            tokens = self.merge_pair_in_tokens(pair, tokens)
        
        return tokens  # моя задача: разбить text на слова, закодировать каждое, но не потерять информацию о границах слов

    def decode(self, tokens: list[str]) -> str:
        return ''.join(tokens)

if __name__ == "__main__":
    tokenizer = BPETokenizer()
    text = "Программирование — это настоящее искусство. Хороший код всегда должен быть чистым, понятным и быстрым. Умные функции принимают разные аргументы, возвращают полезные результаты. Бесконечные циклы перебирают элементы, строгие условия проверяют истину. Ошибки случаются абсолютно у всех, но внимательная отладка всегда помогает найти истинную причину."
    vocab_size = 10
    tokenizer.train(text, vocab_size)
    
    encoded = tokenizer.encode("принимают")
    print("Encoded:", encoded)
    
    decoded = tokenizer.decode(encoded)
    print("Decoded:", decoded)
    print("Merges:", tokenizer.merges)