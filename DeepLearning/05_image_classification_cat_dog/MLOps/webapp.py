#mandatory imports to host the api
from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import io
import sys
import logging
import uvicorn
import tensorflow
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array,load_img
import numpy as np
import shutil
#loading the model
classification_model = tensorflow.keras.models.load_model('TrainedModel.h5')
#classification class
class ClassifyImage:
    #constructor
    def __init__(self,image:np.ndarray):
        self.image = image
    #classifier method
    def classify(self):
          x = np.asarray(self.image.resize((96, 96)))[..., :3]
          x = np.expand_dims(x, axis=0)
          x = preprocess_input(x)
          preds = classification_model.predict(x)
          if float(preds[0][1]) > float(preds[0][0]):
             out_class = "Cat"
          elif float(preds[0][1]) < float(preds[0][0]):
             out_class = "Dog"
          return out_class

#defining the object of FastAPI
classifier_app = FastAPI()

#writing get methods for the classifier_app
@classifier_app.get('/')
def web_app():
    return {'Welcome to the Classifier app'}
#recieving the image from form
@classifier_app.post('/predict')
async def predict_class(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Only use jpg,jpeg or png image to evaluate."
    contents = await file.read()
    #reading the encoded image
    img = Image.open(io.BytesIO(contents))
    #creating an object of classifier
    classifier = ClassifyImage(img)
    label = classifier.classify()
    return {"Predicted Label is {0}".format(label)}

if __name__ == '__main__':
    uvicorn.run(classifier_app,'127.0.0.1')


