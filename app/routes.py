from flask import Blueprint, render_template, request
from .forms import PreferencesForm
from .utils import get_recommendations

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = PreferencesForm()
    if form.validate_on_submit():
        preferences = {
            'top_wear': form.top_wear.data,
            'bottom_wear': form.bottom_wear.data,
            'shoes': form.shoes.data,
            'color': form.color.data
        }
        recommendations = get_recommendations(preferences)
        return render_template('recommendations.html', recommendations=recommendations)
    return render_template('index.html', form=form)
