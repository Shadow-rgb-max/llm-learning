class Tokenizer:
    def __init__(self, vocab_size=1000):
        self.vocab_size = vocab_size
        self.merges = {}  # тут будут храниться правила слияния

    def train(self, text):
        pass  
    
    def encode(self, text):
        pass

    def decode(self, ids):
        pass