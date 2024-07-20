import pickle
import os

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '../ml/models/recommendation_model.pkl')
    with open(model_path, 'rb') as f:
        model, feature_names = pickle.load(f)
    return model, feature_names
