from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length


class CupcakeForm(FlaskForm):
    """form for adding new pet"""
    flavor = StringField('Cupcake Flavor:', validators=[InputRequired()])
    size = StringField('Cupcake Size:',validators=[InputRequired()])
    image = StringField('Photo Url:',validators=[Optional(),URL()])
    rating = IntegerField('Rating:', validators=[NumberRange(min=0,max=20,message='rating must be between 1 and 10'),Optional()])
    
