# -*- coding: utf-8 -*-
#@suraj
#importing modules
import os
import numpy as np
import pandas as pd
!pip install torch
!pip install pytorch-lightning
import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optimizer
from torch.utils.data import Dataset, DataLoader
import pytorch_lightning as py_light
from pytorch_lightning.callbacks import ModelCheckpoint, EarlyStopping
from pytorch_lightning.loggers import TensorBoardLogger
from pytorch_lightning.metrics.functional import accuracy
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

#os.chdir('/content/drive/MyDrive/Colab Notebooks/Dataset/TimeSeriesPrediction')

#!unzip Dataset.zip

"""# About
Recognising the platform where robot is based based on the IMU sensor data.
"""

train_features = pd.read_csv('X_train.csv')

#train_features.head()

train_labels = pd.read_csv('y_train.csv')

#train_labels.head()

print("Shape of training features is {}".format(train_features.shape))
print("Shape of training labels is {}".format(train_labels.shape))

"""# Data interpretation:
For a series of robot's sensor data over various time steps, we will have a surface. This is denoted by series_id in train_features and train_labels and thus the shape of dataframes are not equal. 
"""

#checking the distribution of target variable
train_labels.groupby('surface').count().plot.bar(color='red')

#converting the target variables to categorical variables
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(train_labels.surface)

#encoded_labels.shape

#adding it back to the dataframe
train_labels['platform_label'] = encoded_labels

#train_labels

#processing train+features by dropping the irrelevant ones
feature_cols = train_features.columns.tolist()[3:]

#feature_cols

#checking the number of sensor time steps for each series id
train_features.series_id.value_counts()

#checking if each time step equals 128 for each series id
(train_features.series_id.value_counts()==128).sum() == len(train_labels)

import tqdm
training_dataset = []
for series_id, cols in tqdm.tqdm(train_features.groupby('series_id')):
  sensor_data = cols[feature_cols]
  platform_label = train_labels[train_labels.series_id == series_id].iloc[0].platform_label
  #finally appending
  training_dataset.append((sensor_data, platform_label))

#pd.DataFrame(training_dataset).head()

# doing train_val split
train_sequences, val_sequences = train_test_split(training_dataset, test_size=0.2)
print("shape of train data", np.shape(train_sequences))
print("shape of val data", np.shape(val_sequences))

#defining the data class which inherits the Dataset class
class TrainingDataset(Dataset):
  #defining the constructor
  def __init__(self, sensor_seq):
    self.sensor_seq = sensor_seq

  def __len__(self):
    return len(self.sensor_seq)

  #defining the getter function
  def __getitem__(self,idx):
    self.idx = idx
    sensor_data, platform_label = self.sensor_seq[self.idx]
    #fetched_data = {}
    #fetched_data['sensor_data'] = torch.Tensor(sensor_data.to_numpy())
    #fetched_data['platform_label'] = torch.tensor(platform_label.astype(str).to_numpy())
    #return fetched_data
    return dict(
        sensor_data= torch.Tensor(sensor_data.to_numpy()),
        platform_label= torch.tensor(platform_label)
     )

class TrainDataModule(py_light.LightningDataModule):
  #defining the constructor
  def __init__(self, train_data, val_data, batch):
    #initialising the parent class
    super().__init__()
    self.train_data = train_data
    self.val_data = val_data
    self.batch = batch

  def setup(self, stage=None):
    self.train_data = TrainingDataset(self.train_data)
    self.val_data = TrainingDataset(self.val_data)
    
  #defining the train data loader method
  def train_dataloader(self):
    return DataLoader(self.train_data, batch_size= self.batch, shuffle = True) #, num_workers = 12

  #defining val data loader method
  def val_dataloader(self):
    return DataLoader(self.val_data, batch_size= self.batch, shuffle = False)

data_module = TrainDataModule(train_sequences, val_sequences, 256)

#defining the model

class LSTM_Model(nn.Module):
  #defining the constructor
  def __init__(self, features, classes, hidden_layer = 512, layers = 3):
    #initialising the parent class
    super().__init__()

    self.lstm = nn.LSTM(input_size = features, hidden_size= hidden_layer, num_layers = layers, batch_first =True, dropout=0.5)

    self. classifier_layer = nn.Linear(hidden_layer, classes)

  #defining the forward pass
  def forward(self, x):
    self.lstm.flatten_parameters()
    _, (hidden,_) = self.lstm(x)
    #output will be last label in the sequence
    output = hidden[-1]
    return self.classifier_layer(output)

class Predictor(py_light.LightningModule):

  def __init__(self,n_features, n_classes):
    super().__init__()

    self.model = LSTM_Model(n_features, n_classes)
    #using categorical cross entropy loss
    self.loss = nn.CrossEntropyLoss()
  
  def forward(self, x, label = None):
    output = self.model(x)
    loss = 0 
    if label is not None:
      loss = self.loss(output, label)
    return loss, output

  #defining the training step standard method
  def training_step(self, batch, batch_idx):
    sensor_data = batch['sensor_data']
    gt_label = batch['platform_label']
    loss, output = self(sensor_data, gt_label)
    predicted_label = torch.argmax(output, dim=1)
    #using accuracy of pytorch lightning
    iteration_accuracy = accuracy(predicted_label,gt_label)
    #for tensorboard purposes
    self.log("training loss", loss, prog_bar = True, logger=True)
    self.log("training_loss", iteration_accuracy, prog_bar = True, logger=True)

    return{"loss": loss, "accuracy": iteration_accuracy}

  
  def validation_step(self, batch, batch_idx):
    sensor_data = batch['sensor_data']
    gt_label = batch['platform_label']
    loss, output = self(sensor_data, gt_label)
    predicted_label = torch.argmax(output, dim=1)
    #using accuracy of pytorch lightning
    iteration_accuracy = accuracy(predicted_label,gt_label)
    #for tensorboard purposes
    self.log("val loss", loss, prog_bar = True, logger=True)
    self.log("val_loss", iteration_accuracy, prog_bar = True, logger=True)

    return{"val_loss": loss, "val_accuracy": iteration_accuracy}


  #configuring the optimizer
  def configure_optimizers(self):
    return optimizer.Adam(self.parameters(), lr=1e-5)

model = Predictor(n_features = len(feature_cols), n_classes =len(label_encoder.classes_))

#creating checkpoint call back
checkpoint_callback = ModelCheckpoint(dirpath = "checkpoint", filename= "trained_checkpoint", save_top_k=1, verbose=True, monitor="val_loss", mode="min")

trainer = py_light.Trainer(checkpoint_callback=checkpoint_callback, max_epochs = 10000, gpus=1, progress_bar_refresh_rate=40)

trainer.fit(model, data_module)


# to load from the best checkpoint
# trained_model  =  Predictor.load_from_checkpoint(trainer.checkpoint_callback.best_model_path, n_features = len(feature_cols), n_classes =len(label_encoder.classes_))
# #freezing model
# trained_model.freeze()

# prediction
