import numpy as np
from typing import Tuple

def softmax(x):
    e = np.exp(x - np.max(x))  # вычитаем max для численной стабильности
    return e / e.sum()

def build_vocab(tokens: list[str]) -> Tuple[dict[str, int], dict[int, str]]:
    token_to_id = {token: idx for idx, token in enumerate(set(tokens))}
    id_to_token = {idx: token for token, idx in token_to_id.items()}
    return token_to_id, id_to_token

def forward(center_id: int, in_embed: np.ndarray, out_embed: np.ndarray):
    v = in_embed[center_id]           # [embedding_dim] — вектор центрального слова
    logits = v @ out_embed            # [vocab_size] — сырые оценки для каждого слова
    probs = softmax(logits)           # [vocab_size] — вероятности (используйте вашу softmax из Этапа 0)
    return v, logits, probs

def make_embedding_table(vocab_size: int, embedding_dim: int) -> np.ndarray:
    # пока просто случайные числа — "смысл" появится только после обучения
    return np.random.randn(vocab_size, embedding_dim) * 0.01

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

def cross_entropy_loss(probs: np.ndarray, context_id: int) -> float:
    """
    Вычисляет кросс-энтропийную потерю для предсказанных вероятностей и истинного индекса слова
    
    :param predicted_probs: Массив предсказанных вероятностей для каждого слова в словаре
    :param context_id: Индекс контекстного слова (целое число)
    :return: Значение кросс-энтропийной потери (float)
    """
    # добавляем небольшое значение для предотвращения log(0)
    epsilon = 1e-12
    predicted_probs = np.clip(probs, epsilon, 1. - epsilon)
    
    # Вычисляем кросс-энтропийную потерю
    loss = -np.log(predicted_probs[context_id])
    return loss

def pairs_to_ids(pairs: list[tuple[str, str]], word_to_id: dict[str, int]) -> list[tuple[int, int]]:
    return [(word_to_id[center], word_to_id[context]) for center, context in pairs]

text = "мудрый король правил страной мудрая королева правила страной храбрый король защищал страну храбрая королева защищала страну"
tokens = text.split()

word_to_id, id_to_word = build_vocab(tokens)
pairs = generate_skipgram_pairs(tokens, window_size=2)
id_pairs = pairs_to_ids(pairs, word_to_id)

text = "мудрый король правил страной мудрая королева правила страной храбрый король защищал страну храбрая королева защищала страну"
tokens = text.split()

embedding_dim = 8  # произвольно выбранная размерность (в реальных моделях 100-300)
vocab_size = len(word_to_id)

in_embed = make_embedding_table(vocab_size, embedding_dim)   # [vocab_size, embedding_dim]
out_embed = make_embedding_table(embedding_dim, vocab_size)  # [embedding_dim, vocab_size]



def backward(v : np.ndarray, probs : np.ndarray, context_id : int, out_embed : np.ndarray) -> tuple:
    vocab_size = len(probs)
    
    # градиент по logits - probs - one_hot(context_id)
    d_logits = probs.copy()
    d_logits[context_id] -= 1 
    
    # градиент по v для обновления in_embed[center_id]
    d_v = d_logits @ out_embed.T
    
    # градиент по out_embed
    d_out_embed = np.outer(v, d_logits)
    
    return d_v, d_out_embed

def train_step(center_id : int, context_id : int, in_embed : np.ndarray, out_embed : np.ndarray, lr : float = 0.1) -> float:
    # forward
    v, logits, probs = forward(center_id, in_embed, out_embed)
    loss = cross_entropy_loss(probs, context_id)
    
    # backward
    d_v, d_out_embed = backward(v, probs, context_id, out_embed)
    in_embed[center_id] -= lr * d_v
    out_embed -= lr * d_out_embed
    
    return loss


for epoch in range(1000):
    total_loss = 0
    for center_id, context_id in id_pairs:
        loss = train_step(center_id, context_id, in_embed, out_embed)
        total_loss += loss
    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss:.4f}")

king = in_embed[word_to_id['король']]  # вектор слова "король"
queen = in_embed[word_to_id['королева']]  # вектор слова "королева"
protected = in_embed[word_to_id['защищал']]  # вектор слова "защищал"

print("Vector for 'король':", king)
print("Vector for 'королева':", queen)
print("Vector for 'защищал':", protected)

cos_similarity = np.dot(king, protected) / (np.linalg.norm(king) * np.linalg.norm(protected))
print("Cosine similarity between 'король' and 'защищал':", cos_similarity)
print('the end')