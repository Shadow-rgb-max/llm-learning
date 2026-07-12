from collections import Counter
from itertools import pairwise

def get_pair_freqs_generic(ids: list[int]) -> dict[tuple[int, int], int]:
    pair_freqs = Counter(pairwise(ids))
    return dict(pair_freqs)

def merge_pair_generic(pair: tuple[int, int], ids: list[int], new_id: int) -> list[int]:
    new_ids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and (ids[i], ids[i + 1]) == pair:
            new_ids.append(new_id)
            i += 2
        else:
            new_ids.append(ids[i])
            i += 1
    return new_ids

def train_bytes(byte_ids: tuple[int, ...], vocab_size: int) -> tuple[dict[tuple[int, int], int], list[int]]:
    ids = list(byte_ids)
    merges = {}  # (int, int) -> new_id
    next_id = 256  # первые 256 id уже заняты базовыми байтами

    while next_id < vocab_size:
        pair_freqs = get_pair_freqs_generic(ids)  # аналог вашей get_pair_freqs, но на плоском списке чисел
        if not pair_freqs:
            break
        best_pair = max(pair_freqs, key=pair_freqs.get)
        ids = merge_pair_generic(best_pair, ids, next_id)  # заменяет пару на next_id
        merges[best_pair] = next_id
        next_id += 1

    return merges, ids

result = train_bytes((208, 159, 209, 128, 208, 190, 208, 179, 209, 128, 208, 176, 208, 188, 208, 188, 208, 184, 209, 128, 208, 190, 208, 178, 208, 176, 208, 189, 208, 184, 208, 181, 32, 226, 128, 148, 32, 209, 141, 209, 130, 208, 190, 32, 208, 189, 208, 176, 209, 129, 209, 130, 208, 190, 209, 143, 209, 137, 208, 181, 208, 181, 32, 208, 184, 209, 129, 208, 186, 209, 131, 209, 129, 209, 129, 209, 130, 208, 178, 208, 190, 46, 32), 300)
print("Merges:", result[0])
print("Final IDs:", result[1])

