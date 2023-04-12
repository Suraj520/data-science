#### About
This project illustrates serving a MLflow Model as REST API
Dataset - https://www.kaggle.com/datasets/uciml/iris

1. Train a model using MLproject using the following command
```
mlflow run . --experiment-name trainer
```
2. Mlflow model serve command is used to do the same.
Execute the following command.
```
mlflow models serve --model-uri runs:/d752a07eb7ed48a1b37d1a39eaf9bbe6/model --no-conda
```
3. Access the REST API using the following command since it's exposed to invocations end point.
```
curl -d '{"data":[[5.1,3.5,1.4,0.2]]}' -H 'Content-Type: application/json' localhost:5000/invocations
```
> Note:
If IsADirectoryError errors while serving. use python train.py directly to create mlruns.