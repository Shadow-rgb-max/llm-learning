def merge_pair_in_tokens(pair: tuple[str, str], tokens: list[str]) -> list[str]:
    """Заменяет все вхождения pair на объединённый токен в списке tokens."""
    merged_token = pair[0] + pair[1]
    new_tokens = []
    i = 0
    while i < len(tokens):
        if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == pair:
            new_tokens.append(merged_token)
            i += 2  # пропускаем оба символа пары
        else:
            new_tokens.append(tokens[i])
            i += 1
    return new_tokens

def encode_word(word: str, merges: list[tuple[str, str]]) -> list[str]:
    tokens = list(word)  # разбили на символы
    for pair in merges:  # применяем merges строго в порядке обучения
        tokens = merge_pair_in_tokens(pair, tokens)  # ваша задача написать это
    return tokens

encoded_word = encode_word("программирование", [('а', 'т'), ('е', 'н'), ('н', 'ы'), ('и', 'е'), ('о', 'в'), ('ю', 'т'), ('с', 'л'), ('с', 'т'), ('н', 'о'), ('ны', 'е'), ('р', 'а'), ('с', 'к'), ('и', 'н'), ('м', 'а'), ('н', 'а')])
print(encoded_word)