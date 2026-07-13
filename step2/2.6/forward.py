import numpy as np

def softmax(x):
    e = np.exp(x - np.max(x))  # вычитаем max для численной стабильности
    return e / e.sum()


def forward(center_id: int, in_embed: np.ndarray, out_embed: np.ndarray):
    v = in_embed[center_id]           # [embedding_dim] — вектор центрального слова
    logits = v @ out_embed            # [vocab_size] — сырые оценки для каждого слова
    probs = softmax(logits)           # [vocab_size] — вероятности (используйте вашу softmax из Этапа 0)
    return v, logits, probs

def make_embedding_table(vocab_size: int, embedding_dim: int) -> np.ndarray:
    # пока просто случайные числа — "смысл" появится только после обучения
    return np.random.randn(vocab_size, embedding_dim) * 0.01

embedding_dim = 8  # произвольно выбранная размерность (в реальных моделях 100-300)
vocab_size = 4

in_embed = make_embedding_table(vocab_size, embedding_dim)   # [vocab_size, embedding_dim]
out_embed = make_embedding_table(embedding_dim, vocab_size)  # [embedding_dim, vocab_size]

result = forward(center_id=1, in_embed=in_embed, out_embed=out_embed)
print(result[2])  # печатаем вероятность слова с индексом context_id
