
# Virtual Stylist Web App
A Python web application that recommends outfits based on user preferences and current fashion trends using machine learning.

## 🌟 Features
- Outfit recommendations based on user preferences and fashion trends.
- User-friendly interface with a modern look.
- Responsive design for various devices.
- Developed using Flask, HTML, CSS, and JavaScript.
- Machine learning model to provide smart recommendations.

## 📱 Screens
### Home Screen
- **Outfit Preferences Form**: Users can select their preferences for top wear, bottom wear, shoes, and colors.
- **Submit Button**: Submit the form to get outfit recommendations.

### Recommendations Screen
- Displays recommended outfits based on the user's preferences.
- Each recommendation includes a combination of top wear, bottom wear, and shoes with specified colors.

## 🛠️ Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas
- **Other Libraries**: Flask-WTF for form handling, pickle for model serialization

## 📝 Setup Instructions
Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/obadaKraishan/Virtual_Stylist_Web_App.git
cd Virtual_Stylist_Web_App
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python run.py
```

## 📄 Project Structure
```plaintext
virtual_stylist/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── scripts.js
│   │   └── images/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── recommendations.html
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   └── utils.py
├── ml/
│   ├── fashion_trends.ipynb
│   ├── recommendation_engine.py
│   ├── dataset/
│   │   └── fashion_data_large.csv
│   └── models/
│       └── recommendation_model.pkl
├── tests/
│   ├── test_routes.py
│   └── test_models.py
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## 🎨 Customization
### 1. Update Styles
Modify the styles in `static/css/styles.css` to customize the look and feel of the app.

### 2. Update JavaScript
Adjust the JavaScript in `static/js/scripts.js` for additional interactivity.

### 3. Update Machine Learning Model
Update the machine learning model in `ml/fashion_trends.ipynb` and save the new model to `ml/models/recommendation_model.pkl`.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributors
- [Obada Kraishan](https://github.com/obadaKraishan)
