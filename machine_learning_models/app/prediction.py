import joblib
import numpy as np

class Predict:
    def __init__(self):
        self.model = joblib.load("model/resume_matcher_metadata.pkl")

    def predict_match_score(self, vector_input):
        print(vector_input.shape)
        return self.model.predict([vector_input])[0]

        # vector_input = np.array(vector_input).flatten()
        #
        # if len(vector_input) != 768:
        #     raise ValueError(f"Expected 768 features, got {len(vector_input)}")
        #
        # # Split into 6 equal parts and average each part
        # reduced_features = [vector_input[i * 128:(i + 1) * 128].mean() for i in range(6)]
        #
        # # Predict with the original model
        # return self.model.predict([reduced_features])[0]

