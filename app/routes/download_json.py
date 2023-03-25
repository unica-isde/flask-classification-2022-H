from app import app
from .classifications_id import *

@app.route("/downloadJSON/<string:job_id>", methods=['GET'])
def downloadJSON(job_id):
    """
    API for returning a JSON file with the results of the classification of one job
    """
    data = classifications_id(job_id)['data'] 
    json = {element[0]: element[1] for element in data} #dictionary that iterates over each item in the 'data' list and extracts the first element 
                                                        #element[0] as the key and element[1] as the value
    return json