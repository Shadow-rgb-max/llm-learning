def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

output = list(read_lines('step0/generators/test.py'))
print(output)