from sentence_transformers import SentenceTransformer

class TextVectorizer:
    def __init__(self, model_name='paraphrase-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def text_to_vector(self, text):
        return self.model.encode(text)
