import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

import mlflow
import mlflow.sklearn

if __name__ == "__main__":
    df = pd.read_csv('/home/suraj/ClickUp/Mar-Apr/data/Iris.csv')
    y = df['Species']
    X = df.drop(['Id','Species'], axis = 1) 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    
    model = RandomForestClassifier()
    model.fit(X_train,y_train)
    
    y_pred = model.predict(X_test)
    accuracy= metrics.accuracy_score(y_test, y_pred)
    #recall = metrics.recall_score(y_test,y_pred)
    #precision = metrics.precision_score(y_test,y_pred)
    
    print("accuracy-{}".format(accuracy))

    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")

    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)