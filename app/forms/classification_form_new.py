from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FileField
from wtforms.validators import DataRequired

from config import Configuration

conf = Configuration()


class ClassificationFormNew(FlaskForm):
    model = SelectField('model', choices=conf.models, validators=[DataRequired()])
    image = FileField('image', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
