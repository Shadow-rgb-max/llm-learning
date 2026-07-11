from collections import Counter

def get_pair_count(text : str) -> dict:
    """
    Возвращает словарь, где ключи - это пары элементов из списка,
    а значения - количество их вхождений.
    """
    pair_count = Counter()
    for i in range(len(text) - 1):
        pair = (text[i], text[i + 1])
        pair_count[pair] += 1
    return dict(pair_count)

print(get_pair_count("ГАГУГАГУГ"))  # {'ГА': 3, 'АГ': 2}