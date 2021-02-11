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
#classification function
# def visualize(img):
#   plt.imshow(img)
#   plt.show()
def classify(img):
      x = img_to_array(img)
      x = np.expand_dims(x, axis=0)
      x = preprocess_input(x)
      preds = classification_model.predict(x)
    #print(float(preds[0][1]))
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
@classifier_app.get('/predict')
async def predict_class(image: UploadFile = File(...)):
     #supported extensions
     ext = [".png",".jpg",".JPEG"]
     if image.content_type.endswith(tuple(ext)) is False:
        raise HTTPException(status_code=400, detail=f'File \'{image.filename}\' is not an JPEG,jpg,png image.')
     try:
        contents = await image.read()
        image = Image.open(io.BytesIO(contents)).convert('RGB')
        logging.info("image read")
        image = image.resize((96,96))
        logging.info("image resized to {0}".format(np.shape(image)))
        label = classify(image)
        logging.info("classification label", label)
        return {"Predicted Label is {0}".format(label)}

     except Exception as error:
        logging.exception(error)
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(classifier_app,'127.0.0.1')


