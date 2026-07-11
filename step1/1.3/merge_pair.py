from collections import defaultdict


def merge_pair(pair: tuple[str, str], word_freqs: dict[tuple[str, ...], int]) -> dict[tuple[str, ...], int]:
    """замена всех pair на объединённый токен во всех словах word_freqs."""
    new_word_freqs = defaultdict(int)
    merged_token = pair[0] + pair[1]  # 'a' + 'b' = 'ab'

    for word, freq in word_freqs.items():
        new_word = []
        i = 0
        while i < len(word):
            # проверяем, совпадает ли пара на текущей позиции
            if i < len(word) - 1 and (word[i], word[i+1]) == pair:
                new_word.append(merged_token)
                i += 2  # пропускаем оба символа пары
            else:
                new_word.append(word[i])
                i += 1
        new_word_freqs[tuple(new_word)] = freq
    
    return new_word_freqs