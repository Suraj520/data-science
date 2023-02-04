#imports
import tensorflow.keras as keras
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
#loading the model
model = keras.models.load_model('../model/Signatureverification_updated.h5')
#predicting
image1 = "/path/to/test_image1"
image2 = "/path/to/test_image2"
image1_data = Image.open(image1)
image2_data = Image.open(image2)
#resizing the images
image1_data = image1_data.resize((112,112))
image2_data = image2_data.resize((112,112))
#converting to array
image1_data = img_to_array(image1_data)
image2_data = img_to_array(image2_data)
#converting to float32 datatype
image1_data = np.asarray(image1_data).astype(np.float32)
image2_data = np.asarray(image1_data).astype(np.float32)
image1_data = np.reshape(image1_data,(1,112, 112,3))
image2_data = np.reshape(image2_data,(1,112, 112,3))
print(np.shape(image1_data), np.shape(image2_data))
probability = model.predict([image1_data,image2_data])

if probability > 0.5:
  print("Signs match")
else:
  print("Signs do not match")
