import numpy as np

def softmax(x):
    e = np.exp(x - np.max(x))  # вычитаем max для численной стабильности
    return e / e.sum()

print(softmax(np.array([1.0, 2.0, 4.0])))
# [0.04201007 0.1141952  0.84379473] — сумма = 1