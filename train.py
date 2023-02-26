import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
from catboost import Pool
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import pickle



df = pd.read_csv("final_2019.csv")

df[['month', 'day', 'hour', 'min']] = df[['month', 'day', 'hour', 'min']].astype(str)

#predict delay change
y = df.pop("delay_minutes")

X = df
#print(X.dtypes)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#List of categorical columns
categoricalcolumns = X.select_dtypes(include=["object"]).columns.tolist()
print("Names of categorical columns : ", categoricalcolumns)

#Get location of categorical columns
cat_features = [X.columns.get_loc(col) for col in categoricalcolumns]
print("Location of categorical columns : ",cat_features)


train_data = Pool(data=X_train,
                  label=y_train,
                  cat_features=cat_features
                 )


test_data = Pool(data=X_test,
                  label=y_test,
                  cat_features=cat_features
                 )

#model = CatBoostRegressor(iterations=1000,
 #                         learning_rate=0.1,
  #                        early_stopping_rounds=5,
   #                       depth=10)

model = CatBoostRegressor(iterations=500,
                          learning_rate=0.18,
                          depth = 15,
                          early_stopping_rounds= 5,
                          l2_leaf_reg = 1
                          )

model.fit(X_train, 
          y_train, 
          eval_set=test_data, 
          cat_features=cat_features, 
          plot=True)

rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))
print(rmse)

# Create a dataframe of feature importance 
df_feature_importance = pd.DataFrame(model.get_feature_importance(prettified=True))
#plotting feature importance
plt.figure(figsize=(12, 6));
feature_plot= sns.barplot(x="Importances", y="Feature Id", data=df_feature_importance,palette="cool");
plt.title('features importance');
plt.savefig('feature importance.png');

pred = model.predict(['02','25', '09', '23', 'New Brunswick', 'Edison', 'Northeast Corrdr', '0'])
print(pred)

pickle.dump(model, open('model_final.pkl', 'wb'))