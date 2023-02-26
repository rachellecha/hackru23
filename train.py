import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
from catboost import Pool
import numpy as np
from sklearn.metrics import mean_squared_error
import pickle



df = pd.read_csv("final_2019.csv")

df[['train_id', 'stop_sequence', 'from_id', 'to_id']] = df[['train_id', 'stop_sequence', 'from_id', 'to_id']].astype(str)

#print(df.dtypes)

#predict delay change
y = df.pop("delay_change")

X = df
#print(X.dtypes)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.dtypes)
#print("train data size:",X_train.shape)
#print("test data size:",X_test.shape)


#List of categorical columns
categoricalcolumns = df.columns.tolist()
#print("Names of categorical columns : ", categoricalcolumns)
#Get location of categorical columns
cat_features = [X.columns.get_loc(col) for col in categoricalcolumns]
#print("Location of categorical columns : ",cat_features)

train_data = Pool(data=X_train,
                  label=y_train,
                  cat_features=cat_features
                 )


test_data = Pool(data=X_test,
                  label=y_test,
                  cat_features=cat_features
                 )

model = CatBoostRegressor(iterations=10,
                          learning_rate=1,
                          depth=2)

model.fit(X_train, 
          y_train, 
          eval_set=test_data, 
          cat_features=cat_features, 
          plot=True)

rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))
print(rmse)

model.predict()

