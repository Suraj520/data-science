#### About
> MLFlow Projects
1. It helps one to package data-science project and run it in a standard way by a simple command - mlflow run
2. In this notebook, We'll create a data science project and then create a MLproject.
> Contents of MLProject file
1. name: - To specify name of program (https://mlflow.org/docs/latest/projects.html)
2. execution environment is specified by either local env, conda env or docker inv
like conda_env : my_env.yaml or docker_env : mlflow-docker-example
3. What you want to run is quoted in entry_points :
for ex- main: main function takes in parameters: and command: which are used to quote the input arguments to the command quoted.
> About the project
1. Dataset - https://www.kaggle.com/datasets/aneelaabdullah/regression-techniques-on-house-prices
2. Train using
```
mlflow run . --experiment-name mlflow-project -P estimators=16900 -P max_depth=15 
```
3. Upon execution, It'll yield RUN ID as 
```
Run (ID '68c35bccc3aa47e08b62d915c6e7a935') succeeded
```
4. Use the run id to predict by running
Run
```
 python predict.py --model_uri runs:/68c35bccc3aa47e08b62d915c6e7a935/model
```