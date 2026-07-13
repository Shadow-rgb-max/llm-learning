import numpy as np

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

result = cross_entropy_loss(np.array([0.24991746, 0.25001771, 0.25001222, 0.25005261]), context_id=3)  # пример использования
print(result)  # печатаем значение кросс-энтропийной потери