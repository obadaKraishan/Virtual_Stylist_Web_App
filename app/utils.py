import pandas as pd
import random
from .models import load_model


def get_recommendations(preferences):
    model, feature_names = load_model()

    # Prepare input features for the model
    input_features = {
        'top_wear': preferences['top_wear'],
        'bottom_wear': preferences['bottom_wear'],
        'shoes': preferences['shoes']
    }

    # Handle multi-label color input
    for color in ['Red', 'Blue', 'Black', 'Green', 'Yellow', 'Pink', 'White', 'Gray', 'Purple', 'Orange']:
        input_features[color] = 1 if color in preferences['color'] else 0

    # Convert to DataFrame and match training data format
    input_df = pd.DataFrame([input_features])
    input_df = pd.get_dummies(input_df).reindex(columns=feature_names, fill_value=0)

    # Get predictions from the model
    prediction_probabilities = model.predict_proba(input_df)[0]

    # Define the number of recommendations to provide
    top_n = 5

    # Define possible items and colors for generating recommendations
    top_wear_options = ['Shirt', 'T-shirt', 'Blouse', 'Hoodie', 'Sweater', 'Jacket', 'Tank top', 'Polo', 'Cardigan',
                        'Vest']
    bottom_wear_options = ['Jeans', 'Trousers', 'Shorts', 'Skirt', 'Leggings', 'Sweatpants']
    shoes_options = ['Sneakers', 'Boots', 'Sandals', 'Loafers', 'Derby']
    color_options = ['Red', 'Blue', 'Black', 'Green', 'Yellow', 'Pink', 'White', 'Gray', 'Purple', 'Orange']

    # Generate recommendations with varied items
    recommendations = []
    for i in range(top_n):
        top = random.choice(top_wear_options)
        bottom = random.choice(bottom_wear_options)
        shoes = random.choice(shoes_options)

        top_color = random.choice(preferences['color'])
        bottom_color = random.choice(preferences['color'])
        shoes_color = random.choice(preferences['color'])

        # Ensure unique color combinations
        while len(set([top_color, bottom_color, shoes_color])) < 3:
            top_color = random.choice(preferences['color'])
            bottom_color = random.choice(preferences['color'])
            shoes_color = random.choice(preferences['color'])

        # Generate descriptive recommendations
        outfit = f"You can wear a {top_color} {top} with {bottom_color} {bottom} and {shoes_color} {shoes}."
        recommendations.append(outfit)

    return recommendations
