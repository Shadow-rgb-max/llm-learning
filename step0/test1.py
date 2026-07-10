from collections import Counter

text = "мама мыла раму"
c = Counter(text)
print(c.most_common(3))