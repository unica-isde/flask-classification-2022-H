from flask import render_template
from app import app
from app.forms.histogram_form import HistrogramForm
from config import Configuration

config = Configuration()

@app.route('/histogram', methods=['GET', 'POST'])
def histogram():
    """API for selecting an image and return its image_id to calculate the histogram"""
    form = HistrogramForm()
    if form.validate_on_submit():  # POST
        image_id = form.image.data
        
        # returns the histogram of a specified image 
        return render_template("histogram_output.html", image_id=image_id)

    # otherwise, it is a get request and should return the
    # image selector
    return render_template('histogram_select.html', form=form)
