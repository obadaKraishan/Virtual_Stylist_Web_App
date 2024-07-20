from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.fields import SelectMultipleField
from wtforms.validators import DataRequired
from wtforms.widgets import ListWidget, CheckboxInput

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class PreferencesForm(FlaskForm):
    top_wear = SelectField('Top Wear', choices=[('Shirt', 'Shirt'), ('T-shirt', 'T-shirt'), ('Blouse', 'Blouse'), ('Hoodie', 'Hoodie'), ('Sweater', 'Sweater'), ('Jacket', 'Jacket'), ('Tank top', 'Tank top'), ('Polo', 'Polo'), ('Cardigan', 'Cardigan'), ('Vest', 'Vest')], validators=[DataRequired()])
    bottom_wear = SelectField('Bottom Wear', choices=[('Jeans', 'Jeans'), ('Shorts', 'Shorts'), ('Skirt', 'Skirt'), ('Trousers', 'Trousers'), ('Leggings', 'Leggings'), ('Sweatpants', 'Sweatpants'), ('Chinos', 'Chinos'), ('Capris', 'Capris'), ('Joggers', 'Joggers'), ('Culottes', 'Culottes')], validators=[DataRequired()])
    shoes = SelectField('Shoes', choices=[('Sneakers', 'Sneakers'), ('Boots', 'Boots'), ('Flats', 'Flats'), ('Heels', 'Heels'), ('Sandals', 'Sandals'), ('Loafers', 'Loafers'), ('Moccasins', 'Moccasins'), ('Derby', 'Derby'), ('Oxford', 'Oxford'), ('Brogue', 'Brogue')], validators=[DataRequired()])
    color = MultiCheckboxField('Preferred Colors', choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Black', 'Black'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Pink', 'Pink'), ('White', 'White'), ('Gray', 'Gray'), ('Purple', 'Purple'), ('Orange', 'Orange')])
    submit = SubmitField('Get Recommendations')
