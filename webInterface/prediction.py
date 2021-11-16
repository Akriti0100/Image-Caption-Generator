import os
from PIL import Image
from pickle import load
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.xception import Xception
from .utils import extract_features, generate_desc

def predictCaption(path):
    """Function to generate the caption of the image provided by the user"""

    model_path = os.getcwd() + '\\webInterface\\' + 'model.h5'
    tokenizer_path = os.getcwd() + '\\webInterface\\' + 'tokenizer.p'
    img_path = path
    max_length = 32
    tokenizer = load(open(tokenizer_path,"rb"))
    model = load_model(model_path)
    xception_model = Xception(include_top=False, pooling="avg")
    photo = extract_features(img_path, xception_model)
    img = Image.open(img_path)
    description = generate_desc(model, tokenizer, photo, max_length)
    print("\n\n")
    print(description)
    return description
