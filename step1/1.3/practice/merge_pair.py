from collections import defaultdict

def merge_pair(pair: tuple[str, str], word_freqs: dict[tuple[str, ...], int]) -> dict[tuple[str, ...], int]:
    """Замена всех pair на объединённый токен во всех словах word_freqs."""
    new_word_freqs = defaultdict(int) 
    merged_token = pair[0] + pair[1]
    
    for word, freq in word_freqs.items():
        new_word = []
        i = 0
        # Сокращаем цикл через while + срезы вместо индексации
        while i < len(word):
            if word[i:i+2] == pair:  # Сравнение среза вместо двух индексов
                new_word.append(merged_token)
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        
        new_word_freqs[tuple(new_word)] += freq  
    
    return new_word_freqs

result = merge_pair(('м', 'а'), {('м', 'а', 'м', 'а'): 2, ('м', 'ы', 'л', 'а'): 1, ('р', 'а', 'м', 'у'): 1})
print(result)