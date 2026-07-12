import numpy as np

def make_embedding_table(vocab_size: int, embedding_dim: int) -> np.ndarray:
    # пока просто случайные числа — "смысл" появится только после обучения
    return np.random.randn(vocab_size, embedding_dim) * 0.01

def embed(token_id: int, table: np.ndarray) -> np.ndarray:
    return table[token_id]  # просто индексация по строке