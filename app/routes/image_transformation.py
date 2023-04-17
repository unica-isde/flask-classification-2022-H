from flask import render_template

from app import app
from app.forms.image_transformation_form import ImageTransformationForm
from ml.image_transformation_utils import *
from config import Configuration

config = Configuration()

@app.route('/image_transformation', methods=['GET', 'POST'])
def image_transformation():
    form = ImageTransformationForm()
    # Validate the input 
    if form.validate_on_submit():
        # Get date from the form
        image_id = form.image.data
        transformation_id = form.transformation.data
        transformation_value = form.transformation_value.data

        # Transform the image
        transformed_image = transform_image(image_id=image_id, transformation=transformation_id, 
            value=transformation_value)
        # Get a showable image in webpage after the transformation
        image = get_showable_image(transformed_image)

        # Return the output template
        return render_template('image_transformation_output.html', transformed_image=image)

    # Input is not validated, stay in the form template
    return str(render_template('image_transformation_select.html', 
                           form=form)).replace('step="any"', 'step="0.01"')



