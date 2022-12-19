from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, DecimalField
from wtforms.validators import DataRequired

from app.utils.list_images import list_images
from ml.image_transformation_utils import transformations
from config import Configuration

conf = Configuration()

class ImageTransformationForm(FlaskForm):
    image = SelectField('image', choices=list_images(), validators=[DataRequired()])
    transformation = SelectField('transformation', choices=transformations, validators=[DataRequired()])
    transformation_value = DecimalField(default=1, places=2, rounding=None, use_locale=False, number_format=None, validators=[DataRequired()])
    submit = SubmitField('Submit')
