def text_to_bytes(text: str) -> tuple[int, ...]:
    """Преобразует текст в кортеж байтов."""
    return tuple(text.encode('utf-8'))

text = "Программирование — это настоящее искусство. "
byte_tuple = text_to_bytes(text)
print(byte_tuple)