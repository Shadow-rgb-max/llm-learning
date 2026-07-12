import numpy as np

def one_hot(token_id: int, vocab_size: int) -> np.ndarray:
    vec = np.zeros(vocab_size)
    vec[token_id] = 1
    return vec

def make_embedding_table(vocab_size: int, embedding_dim: int) -> np.ndarray:
    return np.random.randn(vocab_size, embedding_dim) * 0.01

def embed(token_id: int, table: np.ndarray) -> np.ndarray:
    return table[token_id]  # просто индексация по строке

king = one_hot(5, 10)
queen = one_hot(6, 10)
stool = one_hot(2, 10)

embedding_table = make_embedding_table(10, 5)
king_embed = embed(5, embedding_table)
queen_embed = embed(6, embedding_table)
stool_embed = embed(2, embedding_table)

print(np.dot(king_embed, queen_embed))
print(np.dot(king_embed, stool_embed))
print(one_hot(5, 10) @ embedding_table)