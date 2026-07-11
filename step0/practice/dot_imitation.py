def dot(a, b):
    """Вычисляет скалярное произведение двух векторов a и b."""
    assert len(a) == len(b), "Векторы должны быть одинаковой длины"
    return sum(x * y for x, y in zip(a, b))