from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def get_embeddings(self, text_list):
        return self.model.encode(text_list, batch_size=16, convert_to_numpy=True)
