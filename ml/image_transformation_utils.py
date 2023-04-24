from ml.classification_utils import fetch_image 
from PIL import ImageEnhance, Image
from base64 import b64encode
from io import BytesIO

# Transformation names array
transformations = ['COLOR', 'BRIGHTNESS', 'CONTRAST', 'SHARPNESS']

# Transform the image (specified by image_id) applying the transformation at specified value
def transform_image(image_id, transformation, value):
    image = fetch_image(image_id=image_id)
    transformation_effect = transform_step(image, transformation)
    return transformation_effect.enhance(value)

# Transform the given image applying the transformation    
def transform_step(image, transformation):
    if transformation == transformations[0]:
        return ImageEnhance.Color(image)
    elif transformation == transformations[1]:
        return ImageEnhance.Brightness(image)
    elif transformation == transformations[2]:
        return ImageEnhance.Contrast(image)
    elif transformation == transformations[3]:
        return ImageEnhance.Sharpness(image)

# Convert image from bytes to png base64 encoded image
def get_showable_image(image:Image):
    image_data = BytesIO()
    image.save(image_data, 'PNG')
    return "data:%s;base64,%s" % ('image/png', b64encode(image_data.getvalue()).decode('ascii'))