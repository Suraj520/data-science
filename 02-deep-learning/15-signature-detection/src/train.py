# -*- coding: utf-8 -*-
#importing modules
import os
import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import random
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Lambda, Dropout, BatchNormalization
from tensorflow.keras import backend as K
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import img_to_array
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, EarlyStopping, ReduceLROnPlateau, TensorBoard
import pandas as pd
from PIL import Image
import urllib
import tqdm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import time
#reading the data
train_dataset = pd.read_csv('sign_data/train_data.csv')
test_dataset = pd.read_csv('sign_data/test_data.csv')

train_dir = "sign_data/train/"
test_dir = "sign_data/test/"

class DataLoader:
  #constructor
  def __init__(self, dataset, batch_size):
    self.dataset = dataset
    self.batch_size = batch_size
    self.dir = dir
  #shuffler
  def shuffle(self):
    return self.dataset.sample(frac=1)
  #generator
  def datagen(self):
      num_samples = len(self.dataset)
      while True:
        #shuffling the samples
        self.dataset = self.shuffle()
        for batch in range(1, num_samples,self.batch_size):
            image1_batch_samples = self.dir+self.dataset.iloc[:,0][batch:batch+self.batch_size]
            image2_batch_samples = self.dir+self.dataset.iloc[:,1][batch:batch+self.batch_size]
            label_batch_samples = self.dataset.iloc[:,2][batch:batch+ self.batch_size]
            Image1, Image2,Label = [],[],[]
            for image1,image2, label in zip(image1_batch_samples,image2_batch_samples, label_batch_samples):
              #append them to Images directly
              image1_data = Image.open(image1)
              image2_data = Image.open(image2)
              #resizing the images
              image1_data = image1_data.resize((112,112))
              image2_data = image2_data.resize((112,112))
              #converting to array
              image1_data = img_to_array(image1_data)
              image2_data = img_to_array(image2_data)
              Image1.append(image1_data)
              Image2.append(image2_data)
              Label.append(label)
            #convert each list to numpy arrays to ensure that they get processed by fit function
            Image1 = np.asarray(Image1).astype(np.float32)
            Image2 = np.asarray(Image2).astype(np.float32)
            Label = np.asarray(Label).astype(np.float32)
            yield [Image1,Image2], Label

#splitting the dataset into train and val_set
train_set, val_set = train_test_split(train_dataset, test_size=0.25)

#testing datagenerator
train_gen= DataLoader(train_set,train_dir,1024)
val_gen = DataLoader(val_set,train_dir,1024)

[image1, image2], label  = next(train_gen)

#defining siamese model architecture
def custom_siamese_model(input_shape):
  input1 = Input(input_shape)
  input2 = Input(input_shape)
  model = Sequential()
  model.add(Conv2D(16, (3,3), activation='relu', input_shape=input_shape))
  model.add(MaxPooling2D(2,2))
  model.add(Dropout(0.25))

  model.add(Conv2D(32, (3,3), activation='relu'))
  model.add(MaxPooling2D(2,2))
  model.add(Dropout(0.25))

  model.add(Conv2D(64, (3,3), activation='relu'))
  model.add(MaxPooling2D(2,2))
  model.add(Dropout(0.25))

  model.add(Conv2D(128, (3,3), activation='relu'))
  model.add(MaxPooling2D(2,2))
  model.add(Dropout(0.25))

  model.add(Flatten())
  model.add(Dense(512, activation='relu'))
  model.add(Dense(128, activation='relu'))
  embedding1 = model(input1)
  embedding2 = model(input2)
  loss_layer = Lambda(lambda tensors:K.abs(tensors[0] - tensors[1]))
  manhattan_distance =loss_layer([embedding1, embedding2])
  output = Dense(1,activation='sigmoid')(manhattan_distance)
  network = Model(inputs=[input1,input2],outputs=output)
  return network

early_stopper =  EarlyStopping(monitor='val_loss',min_delta=0,patience=3,verbose=1)
custom_callback = [early_stopper]

model = custom_siamese_model((112,112,3))
model.summary()

#defining the optimizer
optimizer = Adam(lr = 1e-4)
model.compile(loss="binary_crossentropy",optimizer=optimizer,metrics=['accuracy'])

print("Initializing Training !!")
history = model.fit_generator(train_gen.datagen(),verbose=1, steps_per_epoch=10000,epochs = 2,validation_data=val_gen.datagen(),validation_steps=1000,callbacks=custom_callback)
#saving model.
model.save('path/to/model')

