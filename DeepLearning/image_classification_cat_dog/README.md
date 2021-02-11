# About 
The jupyter notebook file contains training an EfficientNetB7(Latest architecture) on Dogs and Cats dataset on Google colab.
Trained Model available in release section: 

>> - Trained Model: https://github.com/Suraj520/ML_DL_implementation/releases/tag/TM0.1
>> - Deep Learning Framework used: Keras
>> - Dataset: https://www.kaggle.com/biaiscience/dogs-vs-cats

###### Note: 
> Due to RAM limitations on Google Colab, 1k image per class was used for training and testing. The accuracy was observed to be greater than 95% on both test and val set after fine tuning the imagenet pre-trained weights of EfficientNet.

```You can increase it as per your convenience```

#### Deployment via Fast API
* ```cd MLOps && uvicorn webapp:classifier_app --reload```
<br> ```Ensure that the trained model is placed in MLOps directory```
 * Evaluation
  - Evaluate using FastAPI-Swagger UI in Safari/Chrome.
  ```http://127.0.0.1:8000/docs```
  
 #### Demo video
 <a href="https://drive.google.com/file/d/1FAi5IusVY7-5WlxYokIED1NO4denKIRi/view?usp=sharing"> Link </a>

