from typing import Tuple
import numpy as np

def make_embedding_table(vocab_size: int, embedding_dim: int) -> np.ndarray:
    # пока просто случайные числа — "смысл" появится только после обучения
    return np.random.randn(vocab_size, embedding_dim) * 0.01

def embed(token_id: int, table: np.ndarray) -> np.ndarray:
    return table[token_id]  # просто индексация по строке

def build_vocab(tokens: list[str]) -> Tuple[dict[str, int], dict[int, str]]:
    token_to_id = {token: idx for idx, token in enumerate(set(tokens))}
    id_to_token = {idx: token for token, idx in token_to_id.items()}
    return token_to_id, id_to_token

def generate_skipgram_pairs(tokens: list[str], window_size: int) -> list[tuple[str, str]]:
    pairs = []
    for i, center in enumerate(tokens):
        # Определяем границы окна
        start = max(0, i - window_size)
        end = min(len(tokens), i + window_size + 1)
        
        # Добавляем пары (center, context) для всех контекстных слов в окне
        for j in range(start, end):
            if j != i:  # исключаем центр
                pairs.append((center, tokens[j]))
    return pairs

def pairs_to_ids(pairs: list[tuple[str, str]], word_to_id: dict[str, int]) -> list[tuple[int, int]]:
    return [(word_to_id[center], word_to_id[context]) for center, context in pairs]

pairs = generate_skipgram_pairs(['мудрый', 'король', 'правил', 'страной', 'мудрая', 'королева', 'правила', 'страной', 'храбрый', 'король', 'защищал', 'страну', 'храбрая', 'королева', 'защищала', 'страну'], window_size=2)
word_to_id, id_to_word = build_vocab(['мудрый', 'король', 'правил', 'страной', 'мудрая', 'королева', 'правила', 'страной', 'храбрый', 'король', 'защищал', 'страну', 'храбрая', 'королева', 'защищала', 'страну'])

id_pairs = pairs_to_ids(pairs, word_to_id)
print (id_pairs)

embedding_dim = 8  # произвольно выбранная размерность (в реальных моделях 100-300)
vocab_size = len(word_to_id)

in_embed = make_embedding_table(vocab_size, embedding_dim)   # [vocab_size, embedding_dim]
out_embed = make_embedding_table(embedding_dim, vocab_size)  # [embedding_dim, vocab_size] — обратите внимание на порядок размерностей!

print("in_embed shape:", in_embed.shape)
print("out_embed shape:", out_embed.shape)
