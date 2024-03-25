import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Importing The Models in Scikit-Learn
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# Importing Useful Operators in Scikit-Learn
from sklearn.metrics import r2_score, mean_squared_error
import xgboost as xgb

# Read training and test datasets from Excel files
df_train = pd.read_excel("./train_dataset.xlsx")
# Handling missing values in the training dataset
df_train["wip"] = df_train["wip"].fillna(df_train["wip"].mean())

# Define features (X) and target variable (y) for training
X_train = df_train.iloc[:, :-1]
y_train = df_train["actual_productivity"]

# Instantiate regression models
lr = LinearRegression()
dtr = DecisionTreeRegressor()
knr = KNeighborsRegressor()
rfr = RandomForestRegressor()
svr = SVR()

# Train and evaluate each model
for clf in (lr, knr, dtr, rfr, svr):
    clf.fit(X_train, y_train)
    y_pred_train = clf.predict(X_train)
    print("R2 Score of", clf.__class__.__name__, ":", r2_score(y_train, y_pred_train))

    mse_train = mean_squared_error(y_train, y_pred_train)
    print("Mean Square Error of", clf.__class__.__name__, ":", mse_train)

# Train and evaluate XGBoost model
xgb_r = xgb.XGBRegressor(objective='reg:linear', n_estimators=10, seed=123)
xgb_r.fit(X_train, y_train)
pred_train = xgb_r.predict(X_train)
xgb_mse_train = mean_squared_error(y_train, pred_train)
xgb_r2_train = r2_score(y_train, pred_train)
print("MSE through XGB:", xgb_mse_train)
print("R2 Score through XGB:", xgb_r2_train)
