from transformers import AutoTokenizer, AutoModel
import torch


class BertEmbedder:
    def __init__(self, model_name="bert-base-uncased"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        self.model.eval()  # evaluation mode

    def get_embeddings(self, text):
        # Tokenize
        inputs = self.tokenizer(
            str(text),
            return_tensors="pt",
            truncation=True,
            padding=True
        ).to(self.device)

        # Forward pass without gradients
        with torch.no_grad():
            outputs = self.model(**inputs)

        # Mean pooling
        embeddings = outputs.last_hidden_state.mean(dim=1).cpu().numpy()
        return embeddings
