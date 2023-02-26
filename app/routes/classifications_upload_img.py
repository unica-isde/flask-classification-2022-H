import redis
from flask import render_template
from rq import Connection, Queue
from rq.job import Job

from app import app
from app.forms.classification_form_upload import ClassificationFormUpload
from ml.classification_utils import classify_image
from config import Configuration

import os
from flask import Flask, request
from werkzeug.utils import secure_filename


config = Configuration()

@app.route('/classifications_upload', methods=['GET', 'POST'])
def classificationsNew():
    """API for selecting a model and uploading an image, then running a 
    classification job. Returns the output scores from the 
    model."""
    form = ClassificationFormUpload()
    
    if form.validate_on_submit():  # POST
    
        f = request.files.get('image')
        
        #check if there is a file and if it is an allowed one
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(UPLOAD_FOLDER,filename))
            
            image_id = filename
            model_id = form.model.data
            
            redis_url = Configuration.REDIS_URL
            redis_conn = redis.from_url(redis_url)
            with Connection(redis_conn):
                q = Queue(name=Configuration.QUEUE)
                job = Job.create(classify_image, kwargs={
                    "model_id": model_id,
                    "img_id": image_id
                })
                task = q.enqueue_job(job)

            # returns the image classification output from the specified model
            # return render_template('classification_output.html', image_id=image_id, results=result_dict)
            return render_template("classification_output_queue_upload.html", image_id=image_id, jobID=task.get_id())

    # otherwise, it is a get request and should return the
    # image and model selector
    return render_template('classification_select_upload.html', form=form)


UPLOAD_FOLDER = Configuration.image_folder_path
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

