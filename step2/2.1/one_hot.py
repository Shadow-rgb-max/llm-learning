import numpy as np

def one_hot(token_id: int, vocab_size: int) -> np.ndarray:
    vec = np.zeros(vocab_size)
    vec[token_id] = 1
    return vec

king = one_hot(5, 10)
queen = one_hot(6, 10)
stool = one_hot(2, 10)

print(np.dot(king, queen))  # 0
print(np.dot(king, stool))  # 0