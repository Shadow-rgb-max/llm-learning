def generate_skipgram_pairs(tokens: list, window_size: int) -> list:
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

result = generate_skipgram_pairs(['мудрый', 'король', 'правил', 'страной', 'мудрая', 'королева', 'правила', 'страной', 'храбрый', 'король', 'защищал', 'страну', 'храбрая', 'королева', 'защищала', 'страну'], window_size=2)
print(result)  